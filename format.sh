
python -m black --line-length 120 -C ./smallm
python -m isort --profile black ./smallm
python -m flake8 --config tests/flake8 ./smallm
