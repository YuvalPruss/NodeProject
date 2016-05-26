#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
MySQL Database Worker module.
"""
__author__		=	"Yuval Pruss"
__copyright__	=	"Copyright 2016, The Winner Project"

import MySQLdb

class DB(object):
	def __init__(self, host, user, password, db_name):
		try:		
			#Connection to the database
			self.mydb = MySQLdb.connect(host=host, user=user, passwd=password, db=db_name, \
				charset='utf8', init_command='SET NAMES UTF8')
			#Creating cursor to the database
			self.cursor = self.mydb.cursor()
		except Exception:
			raise ValueError("Database connection error!")

	def exe(self, exe_statemant):
		try:
			#print exe
			self.cursor.execute(exe_statemant)
			self.mydb.commit()
		except Exception:
			raise ValueError("Executing SQL command error!")

	def truncate_table(self, table_name):
		try:
			self.exe('truncate table ' + table_name)
		except Exception:
			raise ValueError('Executing SQL command error!')

	def close(self):
		#Close cursor to the database
		self.cursor.close()	
		#Close connection to the database
		self.mydb.close()

if __name__ == '__main__':
	print "self.cursor -> The cursor to the DB"
	print "self.mydb -> The connector to the DB"