#!/usr/bin/env bash

input_stocks=$1

cd /Users/thomas.mcinally/Documents/Stock-Price-CLI
pipenv run python stockprice.py -stocks ${input_stocks}
