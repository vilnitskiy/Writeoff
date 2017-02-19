MANAGE=python manage.py
flake8=flake8
TEST_APP=syncapp

init:
	$(MANAGE) migrate
run:
	$(flake8)
	$(MANAGE) runserver
run_free:
	$(MANAGE) runserver
pyclean:
	find . -name '*.pyc' -delete
test:
	$(flake8)
	$(MANAGE) test $(TEST_APP)
test_free:
	$(MANAGE) test $(TEST_APP)
