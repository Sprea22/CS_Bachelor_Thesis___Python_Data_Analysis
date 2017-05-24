

----------------------------------------------------------------------------------------------------
||   autoTotal   ||
-------------------
It allows to create a shell script that will execute automatically SIA and MIA for all the Norwegian counties. It can be changed for execute also other dataset's inputs.

./autoTotal.sh

----------------------------------------------------------------------------------------------------
||   autoSingle   ||
-------------------
It allows to create a shell script that will execute automatically SIA and MIA for all the inputs of a specific dataset.

./autoSingle.sh Norway

./autoSingle.sh Troms

----------------------------------------------------------------------------------------------------

####################################################################################################

----------------------------------------------------------------------------------------------------
|| SIA: Single Input Analyzer||
-------------------------------
It allows to do an initial analysis about a specific input of a dataset.

python SIA.py Norway cages

python SIA.py Norway Salmon_price_NOK

python SIA.py Troms cages

python SIA.py Troms averageTemp

----------------------------------------------------------------------------------------------------
|| MIA: Multiple Input Analyzer||
---------------------------------
It allows to do an analysis between all the different inputs of a dataset.

python MIA.py Norway

python MIA.py Troms

----------------------------------------------------------------------------------------------------
|| 	Map	 ||
-------------------
It allows to display a specific parameter using the map of Norway, that is also divided per county.

python Map.py averageTemp

python Map.py biomass

----------------------------------------------------------------------------------------------------
||   Analysis	 ||
-------------------
It allows to display some inputs of a dataset with normalized values in the same graphic.
It's useful for comparing and analyze.

python Analysis.py Norway 2 cages localities

python Analysis.py Troms 3 feedConsumption biomass averageTemp

----------------------------------------------------------------------------------------------------------------------------------------------------------------
||   ARIMA-Evaluate	 ||
---------------------------
It allows to test different configurations of an ARIMA machine using a specific input of a dataset, showing the accuracy with MAPE.

python Arima-Evaluate.py Norway cages

python Arima-Evaluate.py Tromso cages

------------------------------------------------------------
||   ARIMA-Future	 ||
---------------------------
It allows to test a particular ARIMA configuration. It needs in input
- Dataset
- Input
- Number of prediction in the future
- ARIMA configuration order (P,D,Q)

python Arima-Testing.py Norway cages 12 10 1 1

python Arima-Testing.py Tromso cages 12 10 1 1

------------------------------------------------------------

