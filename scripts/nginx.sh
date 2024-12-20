#!/usr/bin/bash

PROJECT_MAIN_DIR_NAME = "guiar-me"

SETUP_CORE = "setup"

sudo systemctl deamon-reload

sudo rm -f /etc/nginx/sites-enabled/default

sudo cp "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/nginx/nginx.conf" "/etc/nginx/sites-available/$SETUP_CORE"

# CREATE SYMBOLIC LINK TO ENABLE NGINX SITE
sudo ln -s "/etc/nginx/sites-available/$SETUP_CORE" "/etc/nginx/sites-enabled"

# ADD WWW_DATA USER TO UBUNTU GROUP
sudo gpasswd -a www-data ubuntu

# RESTART SYSTEM NGINX
sudo systemctl restar nginx

