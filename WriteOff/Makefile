MANAGE=python manage.py
flake8=flake8 --exclude '*migrations*',manage.py

init:
	$(MANAGE) migrate
	$(MANAGE) loaddata fixtures/*.json
run:
	$(MANAGE) runserver
pyclean:
	find . -name '*.pyc' -delete
test:
	$(MANAGE) test
flake8:
	$(flake8)
loaddata:
	$(MANAGE) loaddata fixtures/*.json
