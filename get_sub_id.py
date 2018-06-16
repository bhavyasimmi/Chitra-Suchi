#!/usr/bin/python3

import kairos_face as kf
import json
import mysql.connector as mysql
import cv2
import requests
import mysql.connector as mysql
import datetime

# conn = None
# cursor = None

#initializing enrollment
def init() :

	# global cursor
	# global conn

	# credentials for kairos
	# setting up API keys
	kf.settings.app_id = 'a123a233'
	kf.settings.app_key = '03a5065270150ba0e23a0584ae716b0d'

	try :
		# create a connection with database
		# conn = mysql.connect(user='root',password='root',database='studentdb',host='localhost')
		# cursor = conn.cursor()

		# #check the connection with database
		# if conn.is_connected():
		# 	print("Database Connection is established")
		
			sid = already_registered()
			if	sid != None :
				subid(sid) 
			else :
				return "no sid"

	except kf.exceptions.ServiceRequestError as e1 :
		print(e1)
		return "kairos error"


def already_registered(img_path='user_image.png') :
	#recognizing registered faces
	recognized_faces = kf.recognize_face(file=img_path, gallery_name='members')

	status = recognized_faces['images'][0]['transaction']['status']

	# my changes
	data = json.dumps(recognized_faces)
	dic_data = json.loads(data)
	sid = dic_data['images'][0]['candidates'][0]['subject_id']

	if status == 'success' :
		return sid

	elif status == 'failure' :
		return None

	else :
		return "Retake"


def subid(sub_id):

	conn = mysql.connect(user='bhavya',password='Bhavya1910',database='attendence',host='localhost')

	now = datetime.datetime.today().strftime('%d/%m/%Y')
	print(type(now))
	if conn.is_connected():
		print("Connected")

	cur = conn.cursor()

	sub_id=3
	cur.execute("SELECT * from students where date=%s and rno=%s",(now,sub_id))
	out = cur.fetchall()
	# above out is a list of tuples having date
	print(out)

	if out == [] :
		cur.execute("INSERT into students Values(%s,%s)",(now,int(sub_id)))
		conn.commit()
		print('inserted')

	# count = 0
	# rollno = sub_id
	# print(type(rollno))
	# print(type(sub_id))
	# for i in out:
	# 	count+=1
	# 	if i[0]==now:
	# 		break
	# 	else :
	# 		if count != len(out):
	# 			pass
	# 		else:
	# 			cur.execute('INSERT INTO students(date) Values("%s")'%(now))
	# 			conn.commit()


	# cur.execute("SELECT * from students where date='%s'" %now)
	# output = cur.fetchall()
	# print(type(output[0][1]))
	# if output[0][1]==rollno:
	# 	print("your attendence has been marked")			
	# else:
	# 	print("entered else")
	# 	cur.execute('UPDATE students SET rno=("%s") WHERE date=("%s")' ,(int(rollno),now))
	# 	conn.commit()

	# cur.execute("SELECT * from students")
	# out = cur.fetchall()
	# print(out)
# subid(3)
init()