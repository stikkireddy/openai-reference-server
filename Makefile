# Define the directory containing your Python code
SRC_DIR := .

dev:
	pip install -r dev-requirements.txt

# Define the command to format Python code
fmt: dev
	black $(SRC_DIR)


run:
	python server.py