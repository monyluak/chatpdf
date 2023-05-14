venv:
	python3 -m venv venv

activate:
	source venv/bin/activate

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run: 
	python3 app.py