# Nginx 1.4

## Nginx repo

	echo "deb http://nginx.org/packages/debian/ wheezy nginx" > /etc/apt/sources.list.d/nginx.list
	echo "deb-src http://nginx.org/packages/debian/ wheezy nginx" > /etc/apt/sources.list.d/nginx.list
	wget -qO - http://nginx.org/packages/keys/nginx_signing.key | apt-key add -
	apt-get update

## Install

	apt-get install nginx