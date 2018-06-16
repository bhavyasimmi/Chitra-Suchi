#!/usr/bin/python3

import kairos_face

kairos_face.settings.app_id='745154d5'
kairos_face.settings.app_key='87d08d29db4ab82aed0939fc499c024c'

#ENROLLING NEW FACES

#enrolling from url
#kairos_face.enroll_face(url='http://',subject_id='',gallery_name='my-gallery')

# Enrolling from a file
def enroll(image_path):

	enroll_faces=kairos_face.enroll_face(file=image_path)
	print(enroll_faces)

def detect(image_path):
	# Detect from a file
	detected_faces = kairos_face.detect_face(file=image_path)
	print(detected_faces)
	#print(detected_faces['images'][0]['status'])
	
	if (detected_faces['images'][0]['status']) == 'Complete':

		print("IMAGE IS DETECTED SUCCESSFULLY")
	#else :
	#	print(detected_faces['images'][0]['Message'])
	
def add_face(image_path):
	user_id=input("enter your user_id")
	kairos_face.enroll_face(file=image_path,subject_id=user_id,gallery_name='deepu')
	

def recognize(image_path):
	# Recognizing from a file
	recognized_faces = kairos_face.recognize_face(file=image_path, gallery_name='deepu')
	#print(type(recognized_faces))
	
	#now data in the format of list
	value_list=(recognized_faces.get('images'))
	value_dict=(value_list[0])

	if (value_dict['transaction']['status']) == 'success':
		print("IMAGE IS SUCCESSFULLY RECOGNIZED !!")
		verify(image_path)
	elif(value_dict['transaction']['status']) == 'failure':
		print(value_dict['transaction']['message'])

	else:
		print("SOMETHING WENT WRONG!!")	

	#print(recognized_faces['images']['status'])

	#if (recognized_faces['images'][0]['Status']) == 'success':
	#	print("image is recognized successfully !!")

	#elif (recognized_faces['images'][0]['status']) == 'failure':
	#	print(recognized_faces['images'][0]['message'])

	#else:
	#	print('something went wrong')

def verify(image_path):
	# Verify from a file
	#recognize(image_path)
	user_id=input('enter you user id :')

	verify_faces = kairos_face.verify_face(file=image_path,subject_id=user_id ,gallery_name='deepu')	
	
	#print(verify_faces['images'][0]['transaction']['subject_id'])
	
	if  user_id == (verify_faces['images'][0]['transaction']['subject_id']):
		print("face is verified")

	else:
		print("face is not verified")

	
#choose your option

choice='''
		1. detect
		2. add
		3.recognize
		4.verify
'''

print(choice)

ch=input("enter your choice")

image_path=input("enter the path")

if ch == '1':
	
	detect(image_path)

elif ch == '2':
	
	add_face(image_path)

elif ch == '3':
	recognize(image_path)

elif ch == '4':
	verify(image_path)
else :
	print("something wrong ")