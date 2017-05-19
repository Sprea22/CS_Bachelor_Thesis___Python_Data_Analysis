#!/bin/sh

if [ $1 = "Norway" ]; then
	python SIA.py "$1" price
	python SIA.py "$1" cages
	python SIA.py "$1" localities
	python SIA.py "$1" numberSalmon
	python SIA.py "$1" biomass
	python SIA.py "$1" feedConsumption
	python SIA.py "$1" restock
	python SIA.py "$1" withdrawals
else
	python SIA.py "$1" averageTemp
	python SIA.py "$1" cages
	python SIA.py "$1" localities
	python SIA.py "$1" numberSalmon
	python SIA.py "$1" biomass
	python SIA.py "$1" feedConsumption
	python SIA.py "$1" restock
	python SIA.py "$1" withdrawals

python MIA.py "$1"

fi



