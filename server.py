#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def round_for_a(val, health_a, health_b, max_hitpts):
    
    move_msg='{} \'s move'.format(val)
    pub_a.publish(move_msg)
    listen_a=rospy.wait_for_message('/listen_to_A', String)

    if int(str(listen_a)[7])==1:
        print(val+' attacks all')       
        for j in health_b:
            health_b[j]-=max_hitpts[val]*0.1
    elif int(str(listen_a)[7])==2:
        print(val+' attacks '+str(listen_a)[9:-1])
        for j in health_b:
            if j==str(listen_a)[9:-1]:
                health_b[j]-=max_hitpts[val]*0.2


def round_for_b(val, health_a, health_b, max_hitpts):

    move_msg='{} \'s move'.format(val)
    pub_b.publish(move_msg)
    listen_b=rospy.wait_for_message('/listen_to_B', String)
    if int(str(listen_b)[7])==1:  
        print(val+' attacks all')     
        for j in health_a:
            health_a[j]-=max_hitpts[val]*0.1
    elif int(str(listen_b)[7])==2:
        print(val+' attacks '+str(listen_b)[9:-1])
        for j in health_a:
            if j==str(listen_b)[9:-1]:
                health_a[j]-=max_hitpts[val]*0.2

def round(health_a, health_b, max_hitpts):


    rospy.sleep(2)

    for i in health_a:
        round_for_a(i, health_a, health_b, max_hitpts)
    for i in health_b:
        round_for_b(i, health_a, health_b, max_hitpts)
    
    for i in health_a.copy():
        if health_a[i]<=0:
            health_a.pop(i)
    for j in health_b.copy():
        if health_b[j]<=0:
            health_b.pop(j)

    if len(health_a)==0:
        pub_a.publish(data='You Lose!')
        pub_b.publish(data='You Win!')
        print('Player B Wins!')
    if len(health_b)==0:
        pub_b.publish(data='You Lose!')
        pub_a.publish(data='You Win!')
        print('Player A Wins!')

    return health_a, health_b

def main():
    health_a={'fire':300, 'water':400, 'earth':500}
    health_b={'rock':300, 'thunder':400, 'wind':500}

    max_hitpts={'fire':300, 'water':400, 'earth':500, 'rock':300, 'thunder':400, 'wind':500}

    rospy.init_node('server_node')

    global pub_a
    global pub_b
    global pub_data

    pub_data=rospy.Publisher('/publish_data', String, queue_size=10)
    pub_a=rospy.Publisher('/publish_to_A', String, queue_size=10)
    pub_b=rospy.Publisher('/publish_to_B', String, queue_size=10)
    rospy.sleep(5)
    pub_data.publish('Welcome to Titanic Tussle!')

    rnd=1
    rospy.sleep(2)
    while True:
        print('Round '+str(rnd)+' :')
        pub_data.publish('---------------------------------------')
        rospy.sleep(1)
        pub_data.publish('ROUND'+str(rnd)+' :')
        pub_data.publish('---------------------------------------')
        current_state='Current State:'
        pub_data.publish(current_state)
        for i in health_a:
            pub_data.publish(i+':'+str(health_a[i]))
        for i in health_b:
            pub_data.publish(i+':'+str(health_b[i]))
        pub_data.publish(' ')
        rospy.sleep(2)
        health_a, health_b=round(health_a, health_b, max_hitpts)
        rospy.sleep(2)
        rnd+=1
        if len(health_a)==0 or len(health_b)==0:
            break
        print()
    rospy.spin()

if __name__=="__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass