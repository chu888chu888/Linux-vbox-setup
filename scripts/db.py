#!/usr/bin/python

import MySQLdb as mdb
import sys
import string
import random

def password(size=8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

if sys.argv.__len__() == 0:
	print 'Please specify a new database name'
	sys.exit(2)

root_pass = raw_input("Root Password: ")
db_name = sys.argv[1]
db_pass = password(12)

con = mdb.connect('localhost', 'root', root_pass, 'mysql');

with con:
	cur = con.cursor()
	cur.execute("CREATE DATABASE IF NOT EXISTS `%s`" % db_name)
	cur.execute("CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'" % (db_name, db_pass))
	cur.execute("GRANT ALL PRIVILEGES ON `%s`.* TO '%s'@'localhost'" % (db_name, db_name))

print "Database password: %s" % db_pass
