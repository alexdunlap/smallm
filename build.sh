rm -f ./scripts/python/smallm
ln -s ../../smallm ./scripts/python/smallm
python3 -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install glog==0.3.1
python -m pip install black==25.1.0
python -m pip install isort==6.0.0
python -m pip install flake8==7.1.1
python -m pip install pyyaml==6.0.2
