#!/bin/bash

cd ../src
make
python setup.py register -r pypi
python setup.py sdist upload -r pypi
