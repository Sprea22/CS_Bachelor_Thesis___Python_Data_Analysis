import os
import csv
import sys
import warnings
import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

pyplot.style.use('ggplot')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SPLIT THE INPUT DATASET IN TRAIN & TEST#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def splitDataset(X):
	split_point = int(len(X) * float(0.66))
	train, test = series[0:split_point], series[split_point:]
	train.to_csv("Datasets/train.csv", header=False)
	test.to_csv("Datasets/test.csv", header=False)
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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# EVALUATE COMBINATIONS (P,Q,D) FOR AN ARIMA MODEL #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def predictions_model(dataset, p_values, d_values, q_values):
	dataset = dataset.astype('float32')
	order = (p_values, d_values, q_values)
		# prepare training dataset
	train_size = int(len(dataset) * float(0.66))
	train, test = dataset[0:train_size], dataset[train_size:]
	history = [x for x in train]
	# make predictions
	predictions = list()
	for t in range(len(test)):
		model = ARIMA(history, order=order)
		model_fit = model.fit(disp=0)
		yhat = model_fit.forecast()[0]
		predictions.append(yhat)
		print "Real value:", test[t] , "--> Prediction: ", float(yhat)
		history.append(test[t])
	# calculate out of sample error	
	error = mean_absolute_percentage_error(test, predictions)
	f = open("Datasets/test.csv")
	data = [item for item in csv.reader(f)]
	f.close()
	output(data, predictions)
	print('\n Mean Absolute percentage error (MAPE) = %.3f%%' % (error))
#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# WRITE PREDICTION VALUES INTO A DOCUMENT #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def output(data, predictions):
	new_data = []
	for i, item in enumerate(data):
	    try:
	        item.append(predictions[i][0])
	    except IndexError, e:
	        item.append("placeholder")
	    new_data.append(item)
	filename = "Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv"
	if not os.path.exists(os.path.dirname(filename)):	
		os.makedirs(os.path.dirname(filename))
	f = open("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv", 'w+')
	csv.writer(f).writerows(new_data)
	f.close()
	data = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv")
	data = data.drop(data.columns[1], axis=1)
	data.to_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv", mode ='w', index=False)
#-------------------------------------------------------------------------------------------


# Load current dataset input
series = pd.read_csv("Datasets/"+sys.argv[1]+".csv", usecols=[sys.argv[2]])
yearInput = pd.read_csv("Datasets/" + sys.argv[1]+".csv", usecols=[0])

dataset = series.values
dataset = dataset.astype('float32')
# Method for split the dataset between train and test
splitDataset(series)
train = Series.from_csv("Datasets/train.csv", )
test = Series.from_csv("Datasets/test.csv", )

# Evaluate model with order (p_values, d_values, q_values)
p_values = int(sys.argv[4])
d_values = int(sys.argv[5])
q_values = int(sys.argv[6])
order = (p_values, d_values, q_values)

warnings.filterwarnings("ignore")

#########################################################
# PREDICTION TEST ABOUT HISTORIC VALUES.
#########################################################
predictions_model(dataset, p_values, d_values, q_values)


#########################################################
# PREDICTION ABOUT FUTURE VALUES
#########################################################
# Making the ARIMA Model with the current Dataset and Order previously chosen
model = ARIMA(dataset, order=order)
model_fit = model.fit(disp=0)
# Filling the list "forecast" with the predictions results values
forecast = model_fit.forecast(int(sys.argv[3]))[0]

realValues = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_2015.csv")
realValuesData = realValues[sys.argv[2]].values
realValuesData = realValuesData.astype('float32')

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

realValues= pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", index_col=[0], usecols=[0,1])
predFuture = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", index_col=[0], usecols=[0,2])

predHistoric = pd.read_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv", index_col=[0])
# Reading the predictions results values just saved inside the document
#predFuture = Series.from_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_futurePred.csv", index_col=0, tupleize_cols=True)
# Load the predictions dataset
#predHistoric = Series.from_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_testPred.csv")
#realValues = Series.from_csv("Results_Forecast/"+sys.argv[1]+"/"+sys.argv[1]+"_"+sys.argv[2]+"_2015.csv", header=1)
ax = pyplot.subplot(111)

ax.plot(realValues, "g", label='Real 2015 Values', linewidth=2)
ax.plot(predFuture, "orange", label='Prediction 2015 values', linewidth=2)
ax.plot(predHistoric, "r", label='Prediction test values', linewidth=2)
ax.plot(series, "b", label='Historic values', linewidth=2)
# Plot current input's historic values 
#series.plot(color="blue", linewidth=1.5, label="Series: "+sys.argv[1])
# Plot current input's test prediction
#predHistoric.plot(color="red", linewidth=1.5, label="Prediction test:")
# Plot current input's future prediction
#predFuture.plot(color="green", linewidth=1.5, label="Future Prediction:")
#realValues.plot(color="orange", linewidth=1.5, label="Real 2015 Values")

# Final graphic settings
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True, fontsize=20)

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
pyplot.xlabel("Years")
pyplot.ylabel(sys.argv[2]+" in "+sys.argv[1], fontsize=20)

os.remove("Datasets/train.csv")
os.remove("Datasets/test.csv")
# Display final graphic that compare historic and predicted values
manager = pyplot.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

pyplot.show()