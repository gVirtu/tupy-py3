#!/usr/bin/env bash

pytest -v --pdb --cov=. . \
	--cov-report html \
	--cov-config .coveragerc
