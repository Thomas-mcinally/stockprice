#!/usr/bin/env bash

input_stocks=$1

cd ~/Documents/Terminal-finance
pipenv run python stock.py -stocks ${input_stocks}
