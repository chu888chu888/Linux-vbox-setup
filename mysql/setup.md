# MySQL 5.6

## Dependancies

	aptitude install libaio1

## MySQL User

	groupadd mysql
	useradd -r -g mysql mysql

## Download

	# get a url from http://dev.mysql.com/downloads/mysql/
	wget http://cdn.mysql.com/Downloads/MySQL-5.6/mysql-5.6.12-debian6.0-x86_64.deb

## Install

	dpkg -i mysql-5.6.12-debian6.0-x86_64.deb

## Setup

	cd /usr/local
	ln -s /opt/mysql/server-5.6 mysql
	cd mysql
	./scripts/mysql_install_db --user=mysql
	chown -R root .
	chown -R mysql data
	cp ./support-files/mysql.server /etc/init.d/mysql
	ln -s /usr/local/mysql/bin/* /usr/local/bin/
	service mysql start
	./bin/mysql_secure_installation

## Configure

	mkdir /var/run/mysql
	chown mysql /var/run/mysql
	service mysql restart

### Start at boot

	update-rc.d mysql defaults