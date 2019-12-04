#!/bin/bash

# Tool
# It configures the conda virtual environment for the python3 development. It is not required Python3 is the natively running.

# REQUIREMENTS
  # The conda virtual environment of python3 which is named venv-py3

conda activate venv-py3
export PYTHONPATH=$PWD:$PYTHONPATH

