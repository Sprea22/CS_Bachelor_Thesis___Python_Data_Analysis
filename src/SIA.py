import os
import sys 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as pyplot
from PIL import Image

# Graphic's different design
pyplot.style.use('ggplot')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SINGLE INPUT GRAPHICS OVERVIEW #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def create_single_overview(cols, rows, dest, width, height, listofimages):
    # Setting the images size
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    # Pasting each single picture inside the total overview image
    # using the sizes just calculated.
    for col in range(cols):
        for row in range(rows):
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0


    # Saving the current input overview image
    if dest==0:
        script_dir = os.path.dirname(__file__)
    	results_dir = os.path.join(script_dir, "Results/" + sys.argv[1]+"/"+sys.argv[2]+"/")
    	if not os.path.isdir(results_dir):
    		os.makedirs(results_dir)
        new_im.save(results_dir+"/"+ sys.argv[1] +"_"+sys.argv[2]+"_Graphics_Overview.jpg")
        #new_im.show()
    # Saving the current input overview image in a horizontal format
    if dest==1:
    	script_dir2 = os.path.dirname(__file__)
    	results_dir2 = os.path.join(script_dir2, "Results/" + sys.argv[1]+"/Total_Evidences/Single_Inputs")
    	if not os.path.isdir(results_dir2):
    		os.makedirs(results_dir2)
        new_im.save(results_dir2+"/"+ sys.argv[1] +"_"+sys.argv[2]+"_Overview.jpg")

#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%
# TRENDLINE EQUATION #
#%%%%%%%%%%%%%%%%%%%%%%

def trendlineNorm(x, y):
	z = np.polyfit(x, y, 1)
	return z[0]

def trendline(x, y, col):
    # Add correlation line
	# calc the trendline
	z = np.polyfit(x, y, 1)
	p = np.poly1d(z)
	pyplot.plot(x,p(x), c=col)
	# Display the line equation:
	z2 = trendlineNorm(x, normalization(y))
	return z[0], z2
    
def normalization(values):
	column = list(float(a) for a in range(0, 0))
	val = np.array(values)
	val.astype(float)
	column = val / val.max()
	return column
#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%
# SAVE GRAPHIC LIKE IMAGE#
#%%%%%%%%%%%%%%%%%%%%%%%%%
def saveFigure(descr):
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, "Results/" + sys.argv[1] + "/" + sys.argv[2]+"/")
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
    pyplot.savefig(results_dir + sys.argv[1] +"_"+sys.argv[2]+descr, format="jpg")
#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SAVE CORR COEFF VALUES TO CSV FILE #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def saveMatrix(corrRes, dest):
	mat = np.matrix(corrRes)
	dataframe = pd.DataFrame(data=mat.astype(float))
	dataframe.to_csv(dest, sep=',', header=False, float_format='%.2f', index=False)
#-------------------------------------------------------------------------------------------


#%%%%%%%%%%%%%%%%%
#####  MAIN  #####
#%%%%%%%%%%%%%%%%%
print "-----SIA-----------------------"
print " Elaborating the current input: \n\n Dataset: " + sys.argv[1]
print " Data Input: " + sys.argv[2]
yearInput = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[0])
yearsLen = len(yearInput.values)/12

#%%%%%%%%%%%%%%%%%%
# ANALYSIS PART 1 #
#%%%%%%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Graphic setup about current input with total data.
#-------------------------------------------------------------------------------------------
# Reading the total dataset about the current input.
series1 = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[1,sys.argv[2]])
# Displaying the current plot
series1.plot(color="blue", linewidth=1.5)
years = []
j = 0
# Collecting and displaying the correct values: a plot for values of every single year.
for i in range(len(yearInput)):
    if j==11:
        years.append(yearInput.values[i][0])
        j=0
    else:
        j=j+1 
x = range(0, len(yearInput.values))
pyplot.xticks(np.arange(min(x), max(x)+1, 12.0), years)
# Setting the graphic's title
pyplot.title(sys.argv[1] + "\n" + sys.argv[2]+ ": Total graphic")
series1 = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[sys.argv[2]], squeeze=True)
z1, z2 = trendline(x, series1.values.astype(float), "red")
saveFigure("_Total.jpg")
results_dir = "Results/" + sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_AngCoeff.csv"
with open(results_dir, "w") as text_file:
	text_file.write("," + sys.argv[1] + "-" + sys.argv[2]+"\n")
	text_file.write("Ang_Coeff" + "," + str(z1)+"\n")
	text_file.write("Norma_Ang_Coeff" + "," + str(z2)+"\n")

#%%%%%%%%%%%%%%%%%%
# ANALYSIS PART 2 #
#%%%%%%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Graphic setup about current input for each year.
#-------------------------------------------------------------------------------------------
# Reading the dataset about the current input for each year.
series2 = pd.read_csv("Datasets/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[2]])
# Initialize the graphic's figure
fig2 = pyplot.figure()
ax = fig2.add_subplot(111)
# Set the x axis tick
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
x_pos = np.arange(len(months))
tempValues = []
j = 0
# Collecting and displaying the correct values: a plot for values of every single year.
for i in range(len(series2.values)):
	if j in range(12):
		tempValues.append(series2.values[i][1])
		j = j + 1
		if(i == len(series2.values)-1):
			pyplot.plot(x_pos, tempValues, linewidth=2, alpha=0.8, label = int(series2.values[i-1][0]))
	else:
		pyplot.plot(x_pos, tempValues, linewidth=2, alpha=0.8, label = int(series2.values[i-1][0]))
		tempValues = []
		tempValues.append(series2.values[i][1])
		j = 1

ax.legend(loc=4, ncol=1, fancybox=True, shadow=True)
pyplot.xticks(x_pos,months)
pyplot.xlim(0,11)
pyplot.title(sys.argv[1] + "\n" + sys.argv[2]+ ": Single year's graphic")
pyplot.tight_layout()
saveFigure("_years.jpg")

#%%%%%%%%%%%%%%%%%%
# ANALYSIS PART 3 #
#%%%%%%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Correlation matrix about current input between each year. 
#-------------------------------------------------------------------------------------------
series3 = pd.read_csv("Datasets/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[2]])
# Reading the dataset about the current input between each single year.
corr = []
tempValues = []
j = 0
# Collecting the correct values to elaborate.
for i in range(len(series3.values)+1):
	if j in range(12):
		tempValues.append(series3.values[i][1])
		j = j + 1
	else:
		corr.append(tempValues)
		tempValues = []
		if i in range(len(yearInput)):
			tempValues.append(series3.values[i][1])
			j = 1
# Calculatic che correlation coefficent between each year of the input dataset
corrRes = np.corrcoef(corr)
# Displaying the figure for the current matrix
fig3 = pyplot.figure()
ax = fig3.add_subplot(111)
# Displaying the matrix with the results about correlation coefficents
cax = ax.matshow(corrRes, interpolation='nearest')
# Setting the graphic's title
pyplot.title(sys.argv[1] + "\n" + sys.argv[2]+ ": Correlation between different years")
# Setting the x and y axis of the matrix
x_pos = np.arange(yearsLen)
y_pos = np.arange(yearsLen)
pyplot.yticks(y_pos,years)
pyplot.xticks(x_pos,years)
#cax.set_clim(vmin=0.5, vmax=1)
pyplot.colorbar(cax)
pyplot.tight_layout()
# Saving the current graphic in the right folder
saveFigure("_years_Matrix.jpg")
saveMatrix(corrRes, "Results/"+sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_years_CorrCoeff.csv")


#%%%%%%%%%%%%%%%%%%
# ANALYSIS PART 4 #
#%%%%%%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Correlation matrix about current input between each single month.
#-------------------------------------------------------------------------------------------
# Reading the dataset about the current input for each year.
series4 = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[0,1,sys.argv[2]])
# Calculatic che correlation coefficent between each year of the input dataset
corr = []
for month, year in series4.groupby(["month"], sort=False):
	corr.append(year[sys.argv[2]].values)
corrRes = np.corrcoef(corr)
# Displaying the figure for the current matrix
fig4 = pyplot.figure()
ax = fig4.add_subplot(111)
# Displaying the matrix with the results about correlation coefficents
cax = ax.matshow(corrRes, interpolation='nearest')
# Setting the graphic's title
pyplot.title(sys.argv[1] + "\n" + sys.argv[2]+ ": Correlation between different months")
# Setting the x and y axis of the matrix
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
x_pos = np.arange(len(months))
y_pos = np.arange(len(months))
pyplot.yticks(y_pos,months)
pyplot.xticks(x_pos,months)
#cax.set_clim(vmin=0, vmax=1)
pyplot.colorbar(cax)
pyplot.tight_layout()
saveFigure("_months_Matrix.jpg")
saveMatrix(corrRes, "Results/"+sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_months_CorrCoeff.csv")

#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%
# ANALYSIS PART 5 #
#%%%%%%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Autogenerate the overview image for the current input and update the total overview pdf
#-------------------------------------------------------------------------------------------
# Filling the array with the current input's graphics
listofimages=["Results/" + sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_Total.jpg",
            "Results/" + sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_years_Matrix.jpg", 
            "Results/" + sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_years.jpg",
            "Results/" + sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_months_Matrix.jpg"]

# Updating the current single input overview used in the total overview pdf
create_single_overview(4, 1, 1, 3200, 600, listofimages)
# Creating current single input overview
create_single_overview(2, 2, 0, 1600, 1200, listofimages)


print "\n Done! \n-------------------------------\n################################"
#-------------------------------------------------------------------------------------------