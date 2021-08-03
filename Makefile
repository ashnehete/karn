init:
	virtualenv env && . env/bin/activate
	pip install -r requirements.txt

test:
	. env/bin/activate
	pytest tests --capture=sys -rA

run:
	. env/bin/activate
	python main.py