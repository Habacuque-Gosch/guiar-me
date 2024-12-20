#!/usr/bin/bash
# Exit on error
# set -o errexit

set -e

# URL REPOSITORY
# GIT_REPO_URL = "https://habacuque-gosch@github.com/habacuque-gosch/guiar-me.git" 

# YOUR ACTUAL DIRNAME PROJECT
PROJECT_MAIN_DIR_NAME = "guiar-me"

# CLONE REPOSITORY
# git clone "$GIT_REPO_URL" "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# CHANGE DIRECTORY
cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"
# Convert static asset files

# MAKE ALL .SH FILES
chmod +x scripts/*.sh

# EXECUTE SCRIPTS, PYTHON DEPENDENCIES, GUNICORN, NGINX AND START APP

./scripts/instance_os_dependencies.sh
./scripts/python_dependencies.sh
./scripts/gunicorn.sh
./scripts/nginx.sh
./scripts/start_app.sh

