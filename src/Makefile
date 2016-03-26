PYTHON_SETUP_PY = python setup.py
PYLINT = pylint
COVERAGE_RUN = coverage run --rcfile=coverage.rc -m doctest -vv
COVERAGE_REPORT = coverage report

.PHONY: ci clean dist pylint coverage test report

ci: clean test dist report

clean:
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .cache
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

dist:
	$(PYTHON_SETUP_PY) sdist

pylint:
	$(PYLINT) --rcfile=pylint.rc -j 4 laa

coverage:
	$(COVERAGE_RUN) laa/laa.py

test: pylint coverage

report:
	$(COVERAGE_REPORT)
