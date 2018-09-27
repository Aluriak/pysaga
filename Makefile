

package:
	python -m pysaga



t: test
test:
	python -m pytest -vv --doctest-module --ignore=venv .


.PHONY: package t test
