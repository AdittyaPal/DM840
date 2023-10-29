#!/bin/bash

for levelNum in {1..2};do
	if test "x$levelNum" = "x"; then
		echo "No level number specified.";
		exit 1;
	fi;
	steps=10
	if test "x$steps" = "x"; then
		steps=1000000000
		echo "Be carefull, the number of steps is defaulted to a lot."
	fi;
	mod -e "levelFile = 'levels/level_$levelNum.gml'" -e "steps = $steps" -f doIt.py
	mv "summary/summary.pdf" "results/result_$levelNum.pdf"
done
