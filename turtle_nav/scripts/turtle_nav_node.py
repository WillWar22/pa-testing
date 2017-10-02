#!/usr/bin/env python

import rospy
import math
import numpy as np

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtle_nav.srv import *


class TurtleNav(object):

  def __init__(self):
    rospy.init_node('approach')
    self.goal = Pose() 
    self.velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    self.pose_Subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.goal_callback)
    self.pose = Pose()
    self.goal.x = 1
    self.goal.y = 1
    self.distance = 10
    self.old_dist = 100000000

  def goal_callback(self, curr_pos):
    self.pose = curr_pos
  

  def run(self):
    twist = Twist()
    rate = rospy.Rate(10)
   
    while not rospy.is_shutdown() and self.distance > 1:
       self.distance = abs(self.goal.x - self.pose.x) + abs(self.goal.y - self.pose.y)
       
       #linear velocity
       twist.linear.x = .2 * self.distance
       twist.linear.y = 0  
       twist.linear.z = 0
       #rotational velocity
       twist.angular.z = 4 * (np.arctan2(self.goal.y - self.pose.y, self.goal.x - self.pose.x) - self.pose.theta)

#       if self.goal.y > self.pose.y:
#         if self.goal.x > self.pose.x:
#           if self.old_dist > self.distance:
#             twist.angular.z = (self.goal.y + self.pose.y) * 5/self.distance
#           else:
#             twist.angular.z = 0

#       if self.goal.y < self.pose.y:
#         if self.goal.x < self.pose.x:
#           if self.old_dist > self.distance:
#             twist.angular.z = (self.goal.y - self.pose.y) * 5/self.distance
#           else:
#             twist.angular.z = 0
        
       self.velocity_pub.publish(twist)
#       self.old_dist = self.distance
       rate.sleep()
  
if __name__ == "__main__":
  nav = TurtleNav()
  nav.run()


