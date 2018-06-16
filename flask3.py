#!/usr/bin/python3

from flask import Flask, flash, redirect, render_template, request, session, abort
import os 
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("webcam.html")
 

@app.route("/py")
def camera():
	os.system("python3 /home/deepu/Desktop/html/webcamera.py")
	return "abbhkslxjlkadjclkdjc;dxc;"
 
'''@app.route("/hello/<string:name>/")
def hello(name):
    return render_template ('webcam.html',name=name)'''


if __name__ == "__main__":
    app.run(debug=True)