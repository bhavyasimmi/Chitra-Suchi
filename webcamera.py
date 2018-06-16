#!/usr/bin/python3

import cv2


# start the webcam and read the data into the frame
cap = cv2.VideoCapture(0)
try:
	while True:
		frame = cap.read()[1]
		cv2.imshow("pic",frame)

		if cv2.waitKey(0) & 0xFF == ord('r'):
			cv2.imwrite("afbjgi.png",frame)
			break
		
	cv2.destroyAllWindows()
	cap.release()

except TypeError:
	pass	