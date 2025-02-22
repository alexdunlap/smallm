
python -m black --line-length 120 ./scripts
python -m isort --profile black ./scripts
python -m flake8 --config tests/flake8 ./scripts
