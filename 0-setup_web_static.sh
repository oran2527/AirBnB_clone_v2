#!/usr/bin/env bash
# setup folders for deployment web static
if ! which nginx > /dev/null 2>&1
then
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo chmod 777 /data/web_static/releases/test/index.html
sudo echo "<html>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "  <head>" | sudo tee -a /data/web_static/releases/test/index.html
sudo echo "  </head>" | sudo tee -a /data/web_static/releases/test/index.html
sudo echo "  <body>" | sudo tee -a /data/web_static/releases/test/index.html
sudo echo "    Holberton School" | sudo tee -a /data/web_static/releases/test/index.html
sudo echo "  </body>" | sudo tee -a /data/web_static/releases/test/index.html
sudo echo "</html>" | sudo tee -a /data/web_static/releases/test/index.html
if [[ -L '/data/web_static/current' ]]
then
sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/*
sudo service nginx stop
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /error_404.html;
    location = /error_404.html {
        root /usr/share/nginx/html;
        internal;
    }
    add_header X-Served-By $HOSTNAME;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
