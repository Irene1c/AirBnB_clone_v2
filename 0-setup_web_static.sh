#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create necessary folders
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create file (with simple content, to test your Nginx configuration)
touch /data/web_static/releases/test/index.html

cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create a symbolic link
# If link already exists, it should be deleted and recreated every time the script is ran
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "49a\       location /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
