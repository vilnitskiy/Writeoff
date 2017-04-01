MANAGE=python manage.py
flake8=flake8 --exclude '*migrations*',manage.py
TEST_APP=syncapp

init:
	$(MANAGE) migrate
	$(MANAGE) loaddata fixtures/*.json
run:
	$(MANAGE) runserver
pyclean:
	find . -name '*.pyc' -delete
test:
	$(flake8)
	$(MANAGE) test $(TEST_APP)
test_free:
	$(MANAGE) test $(TEST_APP)
loaddata:
	$(MANAGE) loaddata fixtures/*.json
