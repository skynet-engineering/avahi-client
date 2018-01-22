MODULE=avahi


bootstrap:
	pip install -r requirements.txt

lint:
	flake8 avahi test

test:
	python -m unittest discover -s test -v

docs:
	sphinx-apidoc -o docs ${MODULE}
	mv docs/${MODULE}.rst docs/index.rst
	PYTHONPATH=. sphinx-build -c docs docs docs/build

build:
	python setup.py bdist_wheel --universal

.PHONY: bootstrap lint test docs build
