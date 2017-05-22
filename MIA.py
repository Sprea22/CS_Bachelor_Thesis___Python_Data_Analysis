import numpy as np 
import pandas as pd
from pandas import Series
import matplotlib.pyplot as pyplot
import sys
import matplotlib.ticker as ticker

# Graphic's different design
pyplot.style.use('ggplot')

print "-----MIA-----------------------"
print " Elaborating the current input: \n\n Dataset: " + sys.argv[1]

#%%%%%%%%%%%%%
# MIA PART 1 #
#%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Correlation Matrix about inputs of the current dataset.
#-------------------------------------------------------------------------------------------
# Reading the dataset about the current input for each year.
series = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=range(2,10), header=0)
corr = []
for column in series:
    corr.append(series[column].values)
# Calculatic che correlation coefficent between each year of the input dataset
corrRes = np.corrcoef(corr)

mat = np.matrix(corrRes)
dataframe = pd.DataFrame(data=mat.astype(float))
dataframe.to_csv("Results/"+sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_CorrCoeff.csv", sep=',', header=False, float_format='%.2f', index=False)

fig = pyplot.figure()
ax = fig.add_subplot(111)
# Displaying the matrix with the results about correlation coefficents
cax = ax.matshow(corrRes, interpolation='nearest')
labels = []
j = 1
for i in range(len(series.columns)+1):
		if i == 0:
			labels.append("")
		else:
			labels.append(series.columns[i-1])
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
pyplot.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='left')
pyplot.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
#cax.set_clim(vmin=0.5, vmax=1) 
pyplot.colorbar(cax)
pyplot.title("Correlation Coefficients Matrix - " + sys.argv[1], y=1.15)
pyplot.tight_layout()
pyplot.savefig("Results/" + sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_Total_Matrix.jpg", format="jpg")

#%%%%%%%%%%%%%
# MIA PART 2 #
#%%%%%%%%%%%%%
#-------------------------------------------------------------------------------------------
# Comparison graphic of each input's normalized angular coefficients of the current dataset.
#-------------------------------------------------------------------------------------------
fig2 = pyplot.figure()
ax2 = fig2.add_subplot(111)
temp = [] 
for i in series.columns:
	index = sys.argv[1]+"-"+i
	tempSeries = pd.read_csv("Results/"+sys.argv[1]+"/"+i+"/"+sys.argv[1]+"_"+i+"_AngCoeff.csv", header=0)
	temp.append(tempSeries[index].values[1])
x = range(len(series.columns))

pyplot.barh(x, temp)
# Displaying and saving the bar graphic  
pyplot.yticks(x,series.columns)
pyplot.title("Normalized Angular coefficients - " + sys.argv[1])
pyplot.tight_layout()
pyplot.savefig("Results/"+sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_Norm_Ang_Coeffs.jpg", format="jpg")

print "\n Done! \n-------------------------------\n################################"
