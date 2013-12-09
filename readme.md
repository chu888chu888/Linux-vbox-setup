# Debian (Wheezy) dev box

## Basic Packages

	aptitude install ssh openssh-server ntp ntpdate git

## Packages for working with doc/pdf files

	aptitude install wv poppler-utils

## Set timezone

	dpkg-reconfigure tzdata

## SSH Setup

	ssh-keygen -t rsa

## Networking

	nano /etc/network/interfaces
	service networking restart

# Mount shares

	echo "//x.x.x.x/projects /media/projects cifs guest,uid=www-data,gid=www-data,noserverino 0 0" > /etc/fstab