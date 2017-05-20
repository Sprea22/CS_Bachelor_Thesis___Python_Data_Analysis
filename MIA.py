import numpy as np 
import pandas as pd
from pandas import Series
import matplotlib.pyplot as pyplot
import sys
import matplotlib.ticker as ticker

# Graphic's different design
pyplot.style.use('ggplot')
# Reading the dataset about the current input for each year from 2005 to 2016
series3 = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=range(2,10), header=0)
corr = []
for column in series3:
    corr.append(series3[column].values)
# Calculatic che correlation coefficent between each year of the input dataset
test = np.corrcoef(corr)
fig = pyplot.figure()
ax = fig.add_subplot(111)
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
pyplot.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='left')
pyplot.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
#cax.set_clim(vmin=0.5, vmax=1) 
pyplot.colorbar(cax)
pyplot.title("Correlation Coefficients Matrix - " + sys.argv[1], y=1.15)
pyplot.tight_layout()
pyplot.savefig("Results/" + sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_Total_Matrix.jpg", format="jpg")


fig2 = pyplot.figure()
ax2 = fig2.add_subplot(111)
temp = [] 

for i in series3.columns:
	index = sys.argv[1]+"-"+i
	tempSeries = pd.read_csv("Results/"+sys.argv[1]+"/"+i+"/"+sys.argv[1]+"_"+i+"_AngCoeff.csv", header=0)
	temp.append(tempSeries[index].values[1])
x = range(len(series3.columns))
pyplot.barh(x, temp)
# Displaying and saving the bar graphic  
pyplot.yticks(x,series3.columns)
pyplot.title("Normalized Angular coefficients - " + sys.argv[1])
pyplot.tight_layout()
pyplot.savefig("Results/"+sys.argv[1]+"/Total_Evidences/"+sys.argv[1]+"_Norm_Ang_Coeffs.jpg", format="jpg")

# Showing the graphics to the user if the input choice is equal at "1"

