.PHONY: docs
init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
test:
