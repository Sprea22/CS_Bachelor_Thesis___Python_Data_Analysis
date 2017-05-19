import numpy as np 
import pandas as pd
from pandas import Series
import matplotlib.pyplot as pyplot
import sys
import matplotlib.ticker as ticker

# Graphic's different design
pyplot.style.use('ggplot')
# User input that allowed to DISPLAY AND SAVE the graphic otherwise just SAVE it.
choice = input("Do you want to display the graphic?\n 0 = NO \n 1 = YES\n\n")
# Reading the dataset about the current input for each year from 2005 to 2016
series3 = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=range(2,9), header=0)
corr = []
for column in series3:
    corr.append(series3[column].values)
# Calculatic che correlation coefficent between each year of the input dataset
test = np.corrcoef(corr)
fig2 = pyplot.figure()
ax = fig2.add_subplot(111)
# Displaying the matrix with the results about correlation coefficents
cax = ax.matshow(test, interpolation='nearest')
labels = []
j = 1
for i in range(len(series3.columns)+1):
		if i == 0:
			labels.append("")
		else:
			labels.append(series3.columns[i-1])
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
#cax.set_clim(vmin=0.5, vmax=1) 
pyplot.colorbar(cax)
pyplot.savefig(sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_Total_Matrix.jpg", format="jpg")
# Showing the graphics to the user if the input choice is equal at "1"
if(choice==1):
	pyplot.show()

