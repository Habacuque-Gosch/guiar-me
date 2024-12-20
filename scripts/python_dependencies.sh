#!/usr/bin/env bash

set -e

# PROJECT_MAIN_DIR_NAME = "guiar-me"

# if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
#     echo 'PROJECT_MAIN_DIR_NAME is not set'
#     exit 1
# fi

# CHANGE OWNERSHIP TO UBUNTU USER
sudo chown -R ubuntu:ubuntu "/home/ubuntu/guiar-me"

# CREATE VIRTUAL ENVIRONMENT
echo "CREATE VIRTUAL ENVIRONMENT"
virtualenv "/home/ubuntu/guiar-me/venv"

# ACTIVATE VIRTUAL ENVIRONMENT
echo "ACTIVATE VIRTUAL ENVIRONMENT"
source "/home/ubuntu/guiar-me/venv/bin/activate"

# INSTALL DEPENDENCIES PYTHON
echo "INSTALL DEPENDENCIES PYTHON"
pip install -r "/home/ubuntu/guiar-me/"requirements.txt

echo "DEPENDENCIES INSTALLED SUCCESSFULL."