#!/bin/bash

cd "$(dirname ${0})/.."

echo "Formatting the backend... Our style follows the Black code style."
python -m black gradio test client/python
python -m isort --profile=black gradio test client/python
python -m flake8 --ignore=E731,E501,E722,W503,E126,E203,F403 gradio test client/python --exclude gradio/__init__.py
