PYTHON=python3.7


package:
	$(PYTHON) -m pysaga



t: test
test:
	$(PYTHON) -m pytest -vv --doctest-module --ignore=venv .


.PHONY: package t test


release:
	fullrelease
install_deps:
	- $(PYTHON) -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['install_requires'])" | xargs pip install -U
	- $(PYTHON) -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['test_requires'])" | xargs pip install -U
	- $(PYTHON) -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['packaging_requires'])" | xargs pip install -U
