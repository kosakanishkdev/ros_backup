#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def callback(data):
     rospy.loginfo(' moved  %s', data.data)

def motor():
     rospy.init_node('motor', anonymous = True)
     rospy.Subscriber('values', Float32, callback)
     rospy.spin()

if __name__ == '__main__':
    motor()
    rospy.sleep(1)
