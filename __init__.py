#!/usr/bin/python3

from flask import Flask, flash, redirect, render_template, request, session, abort,Response
import enroll_form
from camera import VideoCamera
 
app = Flask(__name__)
 
camera1 = None
userdata = None

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/enroll", methods=['GET','POST'])
def enroll():
	global userdata

	if request.method=='GET' :
		return render_template("enroll.html")
	elif request.method=='POST' :
		if request.form["action"] == 'SUBMIT':

			userdata = request.form

			return render_template('take_pic.html',result=userdata)

			# status = enroll_form.init(data)
			# if status == mark_attendance :
			# 	pass

		else :
			return "bad request!! Error"
	else :
		return "page not found"

@app.route("/takepic")
def takepic():
	global camera1
	global userdata

	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	camera1.save_image()
	camera1.__del__()
	camera1 = None
	status = enroll_form.init(userdata)
	# userdata = None
	return render_template('take_pic.html',message=status,result=userdata)

@app.route("/cam")
def camera_in_page():
	return "integration in process"

@app.route("/mark_attendance")
def mark_attendance():
	return render_template("mark_attendance.html")

#to open camera in webpage streamed with python
def gen():
	global camera1
	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	while True:
		frame = camera1.get_frame()
		# yield method is used to return without destroying local variable instances
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_image')
def capture_image():
	global camera1
	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	camera1.save_image()
	camera1.__del__()
	camera1 = None
	return "image captured"

if __name__ == "__main__":
    app.run(debug=True)