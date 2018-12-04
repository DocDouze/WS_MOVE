#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


class moveit_test_named_target:


         def __init__(self):

            #First initialize moveit_commander and rospy.
            moveit_commander.roscpp_initialize(sys.argv)
            rospy.init_node('move_group_python_interface_tutorial',anonymous=True)
            #Instantiate a RobotCommander object. This object is an interface to the robot as a whole.
            robot = moveit_commander.RobotCommander()
            #Instantiate a MoveGroupCommander object. This object is an interface to one group of joints.
            group = moveit_commander.MoveGroupCommander("scara_cpe_group")
            #We create this DisplayTrajectory publisher which is used below to publish trajectories for RVIZ to visualize.
            display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=10)

            #
            print "============ Robot Groups:"
            print robot.get_group_names()

            while not rospy.is_shutdown():
                group.set_named_target('left')
                group.go(wait=True)
                rospy.sleep(5)
                group.set_named_target('straight')
                group.go(wait=True)
                rospy.sleep(5)
                group.set_named_target('right')
                group.go(wait=True)
                rospy.sleep(5)


if __name__ == '__main__':
      moveit_test_named_target()
