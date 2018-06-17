#!/usr/bin/python3

import kairos_face as kf
import json
import mysql.connector as mysql
import cv2
import requests
import datetime
from dbconnect import connectdb

conn = None
cursor = None

#initializing enrollment
def init() :

	global cursor
	global conn

	# credentials for kairos
	# setting up API keys
	kf.settings.app_id = 'a123a233'
	kf.settings.app_key = '03a5065270150ba0e23a0584ae716b0d'

	try :
		# create a connection with database
		conn = connectdb()
		cursor = conn.cursor()

		#check the connection with database
		if conn.is_connected():
			print("Database Connection is established")
		
			sid = already_registered()
			if	sid != None :
				return mark_present(sid) 
			elif sid == None :
				return "no_sid"
			else :
				return "no face error"

	except kf.exceptions.ServiceRequestError as e1 :
		print(e1)
		return "kairos error"


def already_registered(img_path='user_img.png') :
	#recognizing registered faces
	recognized_faces = kf.recognize_face(file=img_path, gallery_name='students')

	print(recognized_faces)
	status = recognized_faces['images'][0]['transaction']['status']

	if status == 'success' :
		data = json.dumps(recognized_faces)
		dic_data = json.loads(data)
		sid = dic_data['images'][0]['transaction']['subject_id']
		return sid

	elif status == 'failure' :
		return None

	else :
		return "Retake"

	# my changes
	

	
# checking already enrolled or not and mark attendance
def mark_present(sub_id):

	global conn
	global cursor

	if conn.is_connected():
		print("Connected")

	now = datetime.datetime.today().strftime('%d/%m/%y')

	# checking attendance already marked or not
	cursor.execute("SELECT * from attendance where date=%s and rno=%s",(now,sub_id))
	out = cursor.fetchall()

	if out == [] :
		cursor.execute("INSERT into attendance Values(%s,%s)",(now,int(sub_id)))
		conn.commit()
		return "marked"
	else :
		return "already_marked"