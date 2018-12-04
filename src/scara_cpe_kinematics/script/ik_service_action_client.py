#! /usr/bin/env python

import roslib
roslib.load_manifest('my_dynamixel_tutorial')

import rospy
import actionlib
import math
from scara_cpe_kinematics.srv import GoToXY
from std_msgs.msg import Float64
import trajectory_msgs.msg
import control_msgs.msg
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal

class Joint:

        length_2 = 0.047
        length_1 = 0.08
        
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            self.jta = actionlib.SimpleActionClient('/scara_cpe/scara_cpe_controller/follow_joint_trajectory',FollowJointTrajectoryAction)
            rospy.loginfo('Waiting for joint trajectory action')
            self.jta.wait_for_server()
            rospy.loginfo('Found joint trajectory action!')
            rospy.Service('gotoxy', GoToXY, self.handle_gotoxy)
            


        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()
            goal.trajectory.joint_names = ['shoulder_1_joint', 'shoulder_2_joint']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(3)
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)

        def angles(self,x, y):
            cos_theta2 = (x*x+y*y-self.length_1*self.length_1-self.length_2*self.length_2)/(2*self.length_1*self.length_2)
            sin_theta2 = math.sqrt(1-cos_theta2*cos_theta2)

            theta2 = math.acos(cos_theta2)
            theta1 = math.acos((y*sin_theta2*self.length_2 + x*cos_theta2*self.length_2 + x*self.length_1)/(x*x+y*y))

            return [theta1,theta2]

        def handle_gotoxy(self, req):
            print "Go to :\n " , req
            self.move_joint(self.angles(req.x,req.y))
            return True

def main():
            arm = Joint('f_arm')
            arm.move_joint([0,0])
            rospy.spin()
            
            


if __name__ == '__main__':
      rospy.init_node('joint_position_tester')
      main()