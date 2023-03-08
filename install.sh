#!/usr/bin/env bash
echo  >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "creating alias stockprice=${PWD}/stockprice.sh"
echo "alias stockprice=${PWD}/stockprice.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

touch stockprice.sh
chmod a+x stockprice.sh
echo "#!/usr/bin/env bash" > stockprice.sh
echo "" >> stockprice.sh
echo "input_stocks=\$1" >> stockprice.sh
echo "" >> stockprice.sh
echo "cd ${PWD}" >> stockprice.sh
echo "pipenv run python stockprice.py -stocks \${input_stocks}" >> stockprice.sh



echo "...done"