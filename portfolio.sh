#!/usr/bin/env bash

input_portfolio=$1

cd ~/Documents/Terminal-finance
pipenv run python 02\ -\ portfolio.py -portfolio ${input_portfolio}
