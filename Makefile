help:
	@echo make env
	@echo make install
	@echo make run

env:
	pipenv shell

install:
	pipenv install

run:
	python3 main.py