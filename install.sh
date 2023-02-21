#!/usr/bin/env bash

echo "creating alias stockplot=${PWD}/stockplot.sh"
echo "alias stockplot=${PWD}/stockplot.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "creating alias stock=${PWD}/stock.sh"
echo "alias stock=${PWD}/stock.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "...done"