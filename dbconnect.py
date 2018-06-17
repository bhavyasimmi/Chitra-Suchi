#!/usr/bin/env python3

import mysql.connector as mysql

def connectdb() :

	conn = mysql.connect(user='root',password='root',database='studentdb',host='localhost')

	#check the connection with database
	if conn.is_connected():
		print("Database Connection is established")

	return conn