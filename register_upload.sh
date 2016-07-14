#!/bin/bash

twine register dist/subtitle_joiner-0.1.1.tar.gz
twine register dist/subtitle_joiner-0.1.1-py2.py3-none-any.whl
twine upload dist/*
