#!/usr/bin/bash

# PROJECT_MAIN_DIR_NAME = "guiar-me"

# Copy gunicorn socket and service files
sudo cp "/home/ubuntu/guiar-me/gunicorn/gunicorn.socket" "/etc/systemd/system/gunicorn.socket"
sudo cp "/home/ubuntu/guiar-me/gunicorn/gunicorn.service" "/etc/systemd/system/gunicorn.service"

# Start and enable Gunicorn service
sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

