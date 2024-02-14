create-and-activate-env:
	python -m venv venv
	
install-dependencies: create-and-activate-env
	pip install poetry
	poetry install

start-app:
	uvicorn api.main:app --reload --env-file api/.env
