import cv2
import numpy as np

x = np.ones((1080, 1080))*255
while 1:
	cv2.imshow("img", x)
	k = cv2.waitKey(1)
	if k == 27:
		break
