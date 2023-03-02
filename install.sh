#!/usr/bin/env bash
echo  >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

echo "creating alias stockplot=${PWD}/stockplot.sh"
echo "alias stockplot=${PWD}/stockplot.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

touch stockplot.sh
chmod a+x stockplot.sh
echo "#!/usr/bin/env bash" > stockplot.sh
echo "" >> stockplot.sh
echo "input_ticker=\$1" >> stockplot.sh
echo "" >> stockplot.sh
echo "cd ${PWD}" >> stockplot.sh
echo "pipenv run python stockplot.py -ticker \${input_ticker}" >> stockplot.sh


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