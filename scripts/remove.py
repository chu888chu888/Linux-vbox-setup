#!/usr/bin/python

# setup env
import sys
import os

from subprocess import call

basepath = "/var/www/vhosts"

# get input file
if sys.argv.__len__() == 1:
	print 'Please specify a site name'
	sys.exit(2)

# input file name
site_name = sys.argv[1]

# remove folder
os.system("rm -rf " + basepath + "/" + site_name)

# remove configs
os.system("unlink /etc/nginx/sites-enabled/" + site_name + ".vhost")
os.system("unlink /etc/nginx/sites-available/" + site_name + ".vhost")
#os.system("unlink /etc/php5/fpm/pool.d/" + site_name + ".conf");

os.system("service php5-fpm reload")
os.system("service nginx reload")
