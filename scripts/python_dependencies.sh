#!/usr/bin/env bash

set -e

PROJECT_MAIN_DIR_NAME = "guiar-me"

if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
    echo 'PROJECT_MAIN_DIR_NAME is not set'
    exit 1
fi

# CHANGE OWNERSHIP TO UBUNTU USER
sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# CREATE VIRTUAL ENVIRONMENT
echo "CREATE VIRTUAL ENVIRONMENT"
virtualenv "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv"

# ACTIVATE VIRTUAL ENVIRONMENT
echo "ACTIVATE VIRTUAL ENVIRONMENT"
source "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv/bin/activate"

# INSTALL DEPENDENCIES PYTHON
echo "INSTALL DEPENDENCIES PYTHON"
pip install -r "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/"requirements.txt

echo "DEPENDENCIES INSTALLED SUCCESSFULL."