install:
	pip install -r requirements.txt
	pip install -e .

run:
	start

.PHONY: install run
