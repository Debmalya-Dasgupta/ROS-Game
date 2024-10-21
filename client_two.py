#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_func_all(msg: String):
    print(str(msg)[7:-1])

def callback_func_b(msg: String):
    if str(msg)[7]=='Y':
        print(str(msg)[7:-1])
    else:
        print(str(msg)[7:-1], end=':')
        s=input()
        publish_data.publish(s)

if __name__=="__main__":

    rospy.init_node('client_B')
    global publish_data
    publish_data=rospy.Publisher('/listen_to_B', String, queue_size=10)
    listener_all=rospy.Subscriber('/publish_data', String, callback=callback_func_all)
    listener_b=rospy.Subscriber('/publish_to_B', String, callback=callback_func_b)

    rospy.spin()