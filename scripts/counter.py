#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def timer():
	pub = rospy.Publisher('values', Float32, queue_size = 10)
	rospy.init_node('timer', anonymous = True)
	rate = rospy.Rate(10)
	number = 1
	while not rospy.is_shutdown():
		number = number + 1
		rospy.loginfo(number)
		pub.publish(number)
		rospy.sleep(1)


if __name__ == '__main__':
	try:
		timer()
	except rospy.ROSInterruptException:
		pass
