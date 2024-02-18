create-and-activate-env:
	python -m venv venv
	
install-dependencies: create-and-activate-env
	pip install poetry
	poetry install

start-app:
	uvicorn api.main:app --reload --env-file api/.env

build-dependencies:
	poetry export -f requirements.txt --output requirements.txt

deploy: build-dependencies
	gcloud run deploy sample --port 8080 --source .

logging-gcloud:
	gcloud auth login

config-docker:
	gcloud auth configure-docker

set-region:
	gcloud config set run/region us-east1

