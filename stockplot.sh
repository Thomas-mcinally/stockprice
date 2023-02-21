#!/usr/bin/env bash

input_ticker=$1

cd ~/Documents/Terminal-finance
pipenv run python stockplot.py -ticker ${input_ticker}
