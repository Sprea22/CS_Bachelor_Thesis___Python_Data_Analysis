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
	train.to_csv("Datasets/Output_Files/train.csv", header=False)
	test.to_csv("Datasets/Output_Files/test.csv", header=False)
#-------------------------------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CALCULATED MAPE BETWEEN PREDICTIONS AND REAL VALUES#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def mean_absolute_percentage_error(y_true, y_pred): 
	rng = len(y_true)
	diff = []
	for i in range(0,rng):
		diff.append(y_true[i] - y_pred[i])
		diff[i] = diff[i] / y_true[i]
	abs = np.abs(diff)
	mn = np.mean(abs)
	percentageError = mn * 100
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
	f = open("Datasets/Output_Files/test.csv")
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
	f = open("Results/testPred_"+sys.argv[1]+"_"+sys.argv[2]+".csv", 'w')
	csv.writer(f).writerows(new_data)
	f.close()
	data = pd.read_csv("Results/testPred_"+sys.argv[1]+"_"+sys.argv[2]+".csv")
	data = data.drop(data.columns[1], axis=1)
	data.to_csv("Results/testPred_"+sys.argv[1]+"_"+sys.argv[2]+".csv", mode ='w', index=False)
#-------------------------------------------------------------------------------------------


# Load current dataset input
series = pd.read_csv("Datasets/"+sys.argv[1]+".csv", usecols=[sys.argv[2]])

# Method for split the dataset between train and test
splitDataset(series)

train = Series.from_csv("Datasets/Output_Files/train.csv", )
test = Series.from_csv("Datasets/Output_Files/test.csv", )

# Evaluate model with order (p_values, d_values, q_values)
p_values = int(sys.argv[4])
d_values = int(sys.argv[5])
q_values = int(sys.argv[6])
order = (p_values, d_values, q_values)

warnings.filterwarnings("ignore")
predictions_model(series.values, p_values, d_values, q_values)


dataset = series.values
dataset = dataset.astype('float32')

# Making the ARIMA Model with the current Dataset and Order previously chosen
model = ARIMA(dataset, order=order)
model_fit = model.fit(disp=0)
# Filling the list "forecast" with the predictions results values
forecast = model_fit.forecast(int(sys.argv[3]))[0]

index = []
for i in range(1,int(sys.argv[3])+1):
	index.append(len(dataset) +i)

# Writing the predictions results values inside an output document
rows = zip(index, forecast)
f = open("Results/futurePred_"+sys.argv[1]+"_"+sys.argv[2]+".csv", 'w')
csv.writer(f).writerows(rows)
f.close()



# Reading the predictions results values just saved inside the document
predFuture = Series.from_csv("Results/futurePred_"+sys.argv[1]+"_"+sys.argv[2]+".csv")

# Load the predictions dataset
predHistoric = Series.from_csv("Results/testPred_"+sys.argv[1]+"_"+sys.argv[2]+".csv")

# Plot current input's historic values 
series.plot(color="blue", linewidth=1.5, label="Series: "+sys.argv[1])

# Plot current input's test prediction
predHistoric.plot(color="red", linewidth=1.5, label="Prediction test:")

# Plot current input's future prediction
predFuture.plot(color="green", linewidth=1.5, label="Future Prediction:")

# Final graphic settings
ax = pyplot.subplot(111)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True, fontsize=20)


pyplot.xlabel("Years", fontsize=20)
pyplot.ylabel(sys.argv[1]+" values", fontsize=20)


# Display final graphic that compare historic and predicted values
pyplot.show()