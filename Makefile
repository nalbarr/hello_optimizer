help:
	@echo make install
	@echo make pdm-list
	@echo make run-script-explicit
	@echo make run-module
	@echo make run-script
	@echo make run-module-with-script
	@echo ""
	@echo make clean
	@echo make all
	@echo ""
	@echo make pipx-install
	@echo make run

# NA:
# - NOTE: must have pdm, pipx installed as pre-requisite
#   - i.e., https://pdm-project.org/latest/
#	- i.e., https://github.com/pypa/pipx

# NA
# - default pdm behavior is editable install
#   - i.e., pip install -e .
install: clean
	pdm install

# NA
# - check if hello_optimizer_pdm module as local editable insall
#   
pdm-list:
	pdm list 

# NA
# - exec explicit path runnable script
#   - i.e, pick up __main__.py as (default) runnable module
run-script-explicit:
	@echo "***run-script-explicit"
	python3 ./src/hello_optimizer_python

# NA
# - pick up (default) runnable module
#   - i.e, src/<module_name/__main__.py
# 	- same as
#     - pdm run python -m hello_pdm
run-module: install
	@echo "***run-module"
	python3 -m hello_optimizer_python

# NA
# - exec runnable script
# 	- same as
#     - pdm run python -m hello_pdm.some_script
run-script: install
	@echo "***run-script"
	python3 -m hello_optimizer_python.some_script

all: run-script-explicit \
	run-module \
	run-script \
	run-module-with-script

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .pytest_cache

# NA
# - make pip installable using pipx
pipx-install:
	pipx install . --force

run:
#	.venv/bin/hello-optimizer-python
	hello-optimizer-python
