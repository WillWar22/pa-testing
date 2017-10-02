#!/usr/bin/env python

from turtle_nav.srv import * 
import rospy

def handle_move_turtle_to_goal(req):
  if req.goal_x > 11 or req.goal_x < 0 or req.goal_y > 11 or req.goal_y < 0:
    req.success = False
  else:
    req.success = True

def move_turtle_to_goal_server():
  rospy.init_node('move_turtle_to_goal')
  s = rospy.Service('move_turtle_to_goal', TurtleGoal, handle_move_turtle_to_goal)
  rospy.spin()

if __name__ == "__main__":
  move_turtle_to_goal_server()
