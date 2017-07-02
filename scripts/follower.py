#!/usr/bin/env	python
import	rospy
from	sensor_msgs.msg	import	Image

def	image_callback(msg):
	pass
rospy.init_node('follower')
print("ok1")
image_sub	=	rospy.Subscriber('camera/rgb/image_raw',Image,image_callback)
print("ok2")
rospy.spin()
print("ok3")