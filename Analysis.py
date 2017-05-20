import os
import sys 
import pylab 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as pyplot
from PIL import Image
from fpdf import FPDF
import matplotlib.colors as colors

pyplot.style.use('ggplot')

def normalization(values):
	column = list(float(a) for a in range(0, 0))
	val = np.array(values)
	val.astype(float)
	column = val / val.max()
	return column

def displayScatter(input, col):
	months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	x_pos = np.arange(len(months))
	seriesF = series.values.astype(float)
	test = []
	j = 0
	# Collecting and displaying the correct values: a plot for values of every single year.
	for i in range(len(seriesF)):
		if j in range(12):
			test.append(seriesF[i][1])
			j = j + 1
		else:
			testN = normalization(test)
			pyplot.scatter(x_pos, testN, color=col, s=80, linewidth=2, alpha=0.8, label = input if i==12 else "")
			test = []
			test.append(seriesF[i][1])
			j = 1
	ax2.legend(loc=4, ncol=1, fancybox=True, shadow=True)
	pyplot.xticks(x_pos,months)
	pyplot.title(sys.argv[1])
	pyplot.xlim(0,11)


def displayYears(input, col):
	# Set the x axis tick
	months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	x_pos = np.arange(len(months))
	seriesF = series.values.astype(float)
	test = []
	j = 0
	# Collecting and displaying the correct values: a plot for values of every single year.
	for i in range(len(seriesF)):
		if j in range(12):
			test.append(seriesF[i][1])
			j = j + 1
		else:
			testN = normalization(test)
			pyplot.plot(x_pos, testN, color=col, linewidth=2, alpha=0.8, label = input if i==12 else "")
			test = []
			test.append(seriesF[i][1])
			j = 1
	ax3.legend(loc=4, ncol=1, fancybox=True, shadow=True)
	pyplot.xticks(x_pos,months)
	pyplot.title(sys.argv[1])
	pyplot.xlim(0,11)

def displayTotal(input, col):
	seriesF = series3.values.astype(float)
	pyplot.plot(normalization(seriesF), color=col, linewidth=2, label=input)
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
	pyplot.title(sys.argv[1])
	ax4.legend(loc=4, ncol=1, fancybox=True, shadow=True)
	pyplot.xticks(np.arange(min(x), max(x)+1, 12.0), years)


if(int(sys.argv[2]) >= 1):
	series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[3]])
	# Initialize the graphic's figure
	fig2 = pyplot.figure()
	ax2 = fig2.add_subplot(111)
	displayScatter(sys.argv[3], "blue")

	if(int(sys.argv[2]) >= 2):
		series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[4]])
		displayScatter(sys.argv[4], "red")

		if(int(sys.argv[2]) >= 3):
			series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[5]])
			displayScatter(sys.argv[5], "green")


if(int(sys.argv[2]) >= 1):
	series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[3]])
	# Initialize the graphic's figure
	fig3 = pyplot.figure()
	ax3 = fig3.add_subplot(111)
	displayYears(sys.argv[3], "blue")

	if(int(sys.argv[2]) >= 2):
		series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[4]])
		displayYears(sys.argv[4], "red")

		if(int(sys.argv[2]) >= 3):
			series = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", index_col=['month'], usecols=[0,1,sys.argv[5]])
			displayYears(sys.argv[5], "green")		

if(int(sys.argv[2]) >= 1):
	fig4 = pyplot.figure()
	ax4 = fig4.add_subplot(111)
	yearInput = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=[0])
	yearsLen = len(yearInput.values)/12
	series3 = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=[sys.argv[3]])
	displayTotal(sys.argv[3], "blue")
	
	if(int(sys.argv[2]) >= 2):	
		series3 = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=[sys.argv[4]])
		displayTotal(sys.argv[4], "red")

		if(int(sys.argv[2]) >= 3):
			series3 = pd.read_csv("County_Dataset/" + sys.argv[1]+".csv", usecols=[sys.argv[5]])
			displayTotal(sys.argv[5], "green")

pyplot.show()