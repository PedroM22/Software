#!/usr/bin/env python

import rospy #importar ros para python
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped
class controller(object):
	def __init__(self):
		super(controller, self).__init__()
                self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size = 1)
                self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
                self.twist = Twist2DStamped()



	#def publicar(self):

	def callback(self,msg):
	#rospy.loginfo(msg.axes)
                self.twist.v = 0
                self.twist.omega = 0
		if msg.buttons[0] == 1:
			self.twist.v=10
			print("a")
                elif msg.buttons[1] == 1:
			self.twist.v=-10
			print("b")
		elif msg.buttons[11]==-1:
                        self.twist.omega=-10
			print("<-")
		elif msg.buttons[12]==1:
                        self.twist.omega=10
			print("->")	
		print self.twist	
		self.publisher.publish(self.twist)
	




def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = controller() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
