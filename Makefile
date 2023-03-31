venv0:
	virtualenv venv
	@echo "$  . ./venv/bin/activate"


install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black lib *.py

lint:
	pylint --disable=R,C,W0702,W0621,W1203 lib

refactor: format lint
