#!/bin/bash

# Update package lists
sudo apt-get update -y

# Install Nginx
sudo apt-get install nginx -y

# Modify the default Nginx configuration
echo "Hello World!" | sudo tee /var/www/html/index.html

# Restart Nginx without using systemctl
sudo service nginx restart
