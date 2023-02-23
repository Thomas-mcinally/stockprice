#!/usr/bin/env bash

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


echo "creating alias stock=${PWD}/stock.sh"
echo "alias stock=${PWD}/stock.sh" >> ~/`[[ $SHELL == *"zsh" ]] && echo '.zshrc' || echo '.bashrc'`

touch stock.sh
chmod a+x stock.sh
echo "#!/usr/bin/env bash" > stock.sh
echo "" >> stock.sh
echo "input_stocks=\$1" >> stock.sh
echo "" >> stock.sh
echo "cd ${PWD}" >> stock.sh
echo "pipenv run python stock.py -stocks \${input_stocks}" >> stock.sh



echo "...done"