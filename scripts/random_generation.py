#!/usr/bin/env python3

# BSD-3-Clause License
# Copyright (c) 2022, Ryota Hama and Ryuichi Ueda All rights reserved.

import rospy
from std_msgs.msg import Int32
import random


rospy.init_node('random_generation')
pub = rospy.Publisher('random_num', Int32, queue_size=1)
rate = rospy.Rate(1) 
n = 0

while not rospy.is_shutdown():
    n = random.randint(1, 100)
    pub.publish(n)
    rate.sleep()

