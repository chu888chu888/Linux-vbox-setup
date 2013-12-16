#!/usr/bin/python

# setup env
import os
import zipfile
import MySQLdb as mdb
import sys
import getpass

password = getpass.getpass()
ignore = ["performance_schema","information_schema","mysql"]

basepath = "/var/backups"
mysqlpath = basepath + "/mysql"
datapath = "/var/www"

try:
	con = mdb.connect('localhost', 'root', password, 'mysql');
	cur = con.cursor()
	cur.execute("SHOW DATABASES")

	for i in range(cur.rowcount):
		row = cur.fetchone()
		database = row[0]

		if database not in ignore:
			if not os.path.exists(mysqlpath):
				os.makedirs(mysqlpath)
			filename = "%s/%s.sql.gz" % (mysqlpath, database)
			os.popen("mysqldump -u root -p%s --databases %s | gzip -c > %s" % (password,database,filename))

except mdb.Error, e:
	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

zf = zipfile.ZipFile(basepath + "/www.zip", "w")

for dirname, subdirs, files in os.walk(datapath):
	zf.write(dirname)
	for filename in files:
		zf.write(os.path.join(dirname, filename))

zf.close()