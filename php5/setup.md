# PHP 5.4

## Dotdeb

	echo "deb http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list.d/dotdeb.list
	echo "deb-src http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list.d/dotdeb.list
	wget -qO - http://www.dotdeb.org/dotdeb.gpg | apt-key add -
	apt-get update

## Install packages

	apt-get install \
	php5 php5-common php5-fpm php5-cli \
	php5-curl curl \
	php5-gd php5-imagick \
	php5-intl php5-mcrypt \
	php5-memcache php5-memcached memcached \
	php5-mysqlnd php5-sqlite \
	php5-xmlrpc php5-xsl

## Composer

	curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
	ln -s /usr/bin/composer.phar /usr/bin/composer