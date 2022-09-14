#!/usr/bin/env bash

input_ticker=$1

cd ~/Documents/Terminal-finance
pipenv run python 01\ -\ stock_overview.py -ticker ${input_ticker}
