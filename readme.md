# Debian (Wheezy) dev box

## Basic Packages

	aptitude install ssh openssh-server ntp ntpdate git sysstat

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

# Increase the number of opened files

## Current configuration

Kernel

	cat /proc/sys/fs/file-max

Per process, maximum of opened files a process can have

	ulimit -a | grep "open files"

## Change the current values

	nano  /etc/sysctl.conf
	fs.file-max = 16384
	sysctl -p

	nano /etc/security/limits.conf
	soft nofile 16384
	hard nofile 16384