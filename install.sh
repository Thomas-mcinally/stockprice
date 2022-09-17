#!/usr/bin/env bash

echo "creating alias info=${PWD}/stock_overview.sh"
echo "alias info=${PWD}/stock_overview.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "creating alias portfolio=${PWD}/portfolio.sh"
echo "alias portfolio=${PWD}/portfolio.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "...done"