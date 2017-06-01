import os
import csv
import sys
import warnings
import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA

pyplot.style.use('ggplot')

#-------------------------------------------------------------------------------------------
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CALCULATED MAPE BETWEEN PREDICTIONS AND REAL VALUES#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def mean_absolute_percentage_error(y_true, y_pred): 
	try:
		rng = len(y_true)
		diff = []
		for i in range(0,rng):
			diff.append(y_true[i] - y_pred[i])
			diff[i] = diff[i] / y_true[i]
		abs = np.abs(diff)
		mn = np.mean(abs)
		percentageError = mn * 100
	except:
		rng = 0
		abs = np.abs((y_true-y_pred)/y_true)
		percentageError = abs * 100
	return percentageError
#-------------------------------------------------------------------------------------------

# Load current dataset input
series = pd.read_csv("Datasets/"+sys.argv[1]+".csv", usecols=[sys.argv[2]])
yearInput = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[0])

# Reading the real future values 
realValues = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_2015.csv", usecols=[0,1,"feedConsumption"])

# Initial datasets configurations.
realValuesData = realValues[sys.argv[2]].values
realValuesData = realValuesData.astype('float32')
dataset = series.values
dataset = dataset.astype('float32')

# Evaluate model with order (p_values, d_values, q_values)
p_values = int(sys.argv[4])
d_values = int(sys.argv[5])
q_values = int(sys.argv[6])
order = (p_values, d_values, q_values)
warnings.filterwarnings("ignore")


##################################
# PREDICTION ABOUT FUTURE VALUES #
##################################
# Making the ARIMA Model with the current Dataset and Order previously chosen
model = ARIMA(dataset, order=order)
model_fit = model.fit(disp=0)
# Filling the list "forecast" with the predictions results values
forecast = model_fit.forecast(int(sys.argv[3]))[0]

# Preparing the data that are going to be written in the output document that contains the results.
index = []
for i in range(1,int(sys.argv[3])+1):
	index.append(len(dataset) +i)
mape_list = []
for i in range(0,len(forecast)):
	mape_list.append(mean_absolute_percentage_error(realValuesData[i], forecast[i]))

# Writing the predictions results values inside an output document
rows = zip(index, realValuesData, forecast, mape_list)
f = open("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", 'w')
csv.writer(f).writerows(rows)
f.close()

# Reading the real future values from the reported document
realValues= pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", index_col=[0], usecols=[0,1])
# Reading the predicted future values from the reported document
predFuture = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", index_col=[0], usecols=[0,2])

# Initializing output graphic
pyplot.figure()
ax = pyplot.subplot(111)
pyplot.tight_layout()

# Displaying the real future values plot, green color.
ax.plot(realValues, "g", label='Real 2015 Values', linewidth=2)
# Displaying the predicted future values plot, red color.
ax.plot(predFuture, "r", label='Predicted 2015 Values', linewidth=2)
# Displaying the historic values plot, blue color.
ax.plot(series, "b", label='Historic Values', linewidth=2)
# Graphic legend settings
ax.legend(loc='lower right', ncol=1, fancybox=True, shadow=True, fontsize=20)

# Displaying current years on the xlabel.
years = []
j = 0
for i in range(len(yearInput)):
    if j==11:
        years.append(yearInput.values[i][0])
        j=0
    else:
        j=j+1 
x = range(0, len(yearInput.values))
pyplot.title(sys.argv[1] + " - " + sys.argv[2] + " | ARIMA order: " + str(order), fontsize=20)
pyplot.xticks(np.arange(min(x), max(x)+1, 12.0), years)
pyplot.xlabel("Years")
pyplot.ylabel(sys.argv[2]+" in "+sys.argv[1], fontsize=20)

# Display final graphic in full screen mode
manager = pyplot.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
pyplot.show()
