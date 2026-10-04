'''Face Recognition Main File'''
import cv2
import time
import numpy as np
import glob
import imutils
import time
import os
from scipy.spatial import distance
from imutils import face_utils
from keras.models import load_model
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from imutils.video import VideoStream
from flask import Flask,render_template,Response
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://srp23:1234@srp2.dz2nxg7.mongodb.net/?retryWrites=true&w=majority")
db = cluster["SVEC"]
collection = db["Students"]

app=Flask(__name__)
video_capture=cv2.VideoCapture(0)
FR_model = load_model('nn4.small2.v1.h5')
#print("Total Params:", FR_model.count_params())

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

threshold = 0.25

face_database = {}

for name in os.listdir('images'):
	for image in os.listdir(os.path.join('images',name)):
		identity = os.path.splitext(os.path.basename(image))[0]
		face_database[identity] = fr_utils.img_path_to_encoding(os.path.join('images',name,image), FR_model)

def detect_face():
	#print(face_database)
	global rollnumber
	#video_capture = cv2.VideoCapture(0)
	while True:
		ret, frame = video_capture.read()
		frame = cv2.flip(frame, 1)

		faces = face_cascade.detectMultiScale(frame, 1.3, 5)
		for(x,y,w,h) in faces:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
			roi = frame[y:y+h, x:x+w]
			encoding = img_to_encoding(roi, FR_model)
			min_dist = 100
			identity = None

			for(name, encoded_image_name) in face_database.items():
				dist = np.linalg.norm(encoding - encoded_image_name)
				if(dist < min_dist):
					min_dist = dist
					identity = name
				#print('Min dist: ',min_dist)

			if min_dist < 0.1:
				cv2.putText(frame, identity[:-1], (x, y - 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0, 0), 2)
				rollnumber = identity[:-1]
				#cv2.putText(frame, "Dist : " + str(min_dist), (x, y - 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
			else:
				rollnumber = 0
				cv2.putText(frame, 'No matching faces', (x, y - 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
		ret,buffer=cv2.imencode('.jpg',frame)
		frame=buffer.tobytes()
		yield(b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def display_student(roll):
	if roll == 0:
		return "Face not registered"
	student = collection.find_one({"rollno":roll})
	answer = '<p style="font-size: 40px;"><b>Name: </b>'+student["name"]+ \
	'<br><b>Roll Number: </b>'+student['rollno']+ \
	'<br><b>Branch: </b>'+student['branch']+\
	'<br><b>Year of joining: </b>'+student['year']+\
	'<br><b>Attendance percentage:</b> '+student['attendance']+\
	'<br><b>Number of backlogs: </b>'+student['backlogs']+\
	'<br><b>Date of birth:</b> '+student['dob']+\
	'<br><b>Email: </b>'+student['email']+\
	'<br><b>Mobile No.: </b>'+student['mobileno']+"</p>"
	return answer
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livestream')
def livestream():
	return render_template('livestream.html')
	
@app.route('/video')
def video():
    return Response(detect_face(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/display', methods=["GET","POST"])
def display():
	return Response(display_student(rollnumber))

if __name__=="__main__":
    app.run(debug=True)