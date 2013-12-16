#!/usr/bin/python

# setup env
import sys
import os

from subprocess import call

basepath = "/var/www/vhosts"

# get input file
if sys.argv.__len__() == 1:
	print 'Please specify a new site name'
	sys.exit(2)

# input file name
site_name = sys.argv[1]

# create output folder
if not os.path.exists(basepath + "/" + site_name):
	os.makedirs(basepath + "/" + site_name)
	os.makedirs(basepath + "/" + site_name + "/public")

# default welcome
index = "<?php echo 'Welcome to " + site_name + "';"

# write index
output_file = open(basepath + "/" + site_name + "/public/index.php", 'w')
output_file.write(index)
output_file.close()

# set permissions
os.system("chown -R www-data:www-data " + basepath + "/"  + site_name)

# nginx conf
vhost = "server {\n"
vhost += "\tlisten 80;\n"
vhost += "\tserver_name " + site_name + ";\n"
vhost += "\troot " + basepath + "/" + site_name + "/public;\n"
vhost += "\tindex index.php index.html;\n"
vhost += "\tinclude conf.d/bp.conf;\n"
vhost += "\tinclude conf.d/php.conf;\n"
vhost += "}"

# write vhost
output_file = open("/etc/nginx/sites-available/" + site_name + ".vhost", 'w')
output_file.write(vhost)
output_file.close()

'''
# php5-fpm conf
fpm = "[" + site_name + "]\n"
fpm += "user = www-data\n"
fpm += "group = www-data\n"
fpm += "listen = 127.0.0.1:9000\n"
fpm += "listen.allowed_clients = 127.0.0.1\n"
fpm += "pm = static\n"
fpm += "pm.max_children = 2\n"
fpm += "chdir = /"

# write fpm
output_file = open("/etc/php5/fpm/pool.d/" + site_name + ".conf", 'w')
output_file.write(fpm)
output_file.close()
'''

# enable and reload
os.system("ln -s ../sites-available/" + site_name + ".vhost /etc/nginx/sites-enabled")
os.system("service php5-fpm reload")
os.system("service nginx reload")
