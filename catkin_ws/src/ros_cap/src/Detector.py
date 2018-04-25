#!/usr/bin/env python

import rospy #importar ros para python
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
class cam(object):
	def __init__(self):
		super(cam, self).__init__()
                self.publisher = rospy.Publisher("/duckiebot/filtro", Image, queue_size = 10)
                self.subscriber = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
                self.Twist = Image()



	#def publicar(self)

	def callback(self,msg):
		bridge = CvBridge()
		image=bridge.imgmsg_to_cv2(msg, "bgr8")
		image_out = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(image_out,np.array([15,150,150]),np.array([50,255,255]))
		image_out2 = cv2.bitwise_and(image_out,image_out,mask=mask)
		kernel=np.ones((7,7),np.uint8)
		image_out3 = cv2.erode(image_out2,kernel,iterations = 1)
		image_out4 = cv2.dilate(image_out3,kernel,iterations = 2)
		(_,contours,hierarchy)=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		z=image.copy()
		for c in contours:
			area=cv2.contourArea(c)
			if area >=100:
				x,y,w,h = cv2.boundingRect(c)
				z=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
		k=bridge.cv2_to_imgmsg(z,"bgr8")
		self.publisher.publish(k)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = cam() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
