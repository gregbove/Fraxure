.PHONY: run clean

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

venv: venv/touchfile
	source venv/bin/activate
	$(PYTHON) backend/app/app.py

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

run:
	$(PYTHON) backend/app/app.py

clean:
	rm -rf $(VENV)
	find -iname "__pycache__" -delete
	find -iname "*.pyc" -delete
