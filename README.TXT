
----------------------------------------------------------------------------------------------------

./autoTotal.sh

----------------------------------------------------------------------------------------------------

./autoSingle.sh Norway

./autoSingle.sh Troms

----------------------------------------------------------------------------------------------------

python SIA.py Norway cages

python SIA.py Norway Salmon_price_NOK

python SIA.py Troms cages

python SIA.py Troms averageTemp

----------------------------------------------------------------------------------------------------

python MIA.py Norway

python MIA.py Troms

----------------------------------------------------------------------------------------------------

python Map.py averageTemp

python Map.py biomass

----------------------------------------------------------------------------------------------------

python Analysis.py Norway 2 cages localities

python Analysis.py Troms 3 feedConsumption biomass averageTemp

----------------------------------------------------------------------------------------------------------------------------------------------------------------

python Arima-Evaluate.py Norway cages

python Arima-Evaluate.py Tromso cages

------------------------------------------------------------

python Arima-Testing.py Norway cages 12 10 1 1

python Arima-Testing.py Tromso cages 12 10 1 1

------------------------------------------------------------

