#! /usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


class moveit_test_fails:


         def __init__(self):
            print "============ Starting tutorial setup"
            moveit_commander.roscpp_initialize(sys.argv)
            rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)
            robot = moveit_commander.RobotCommander()
            group = moveit_commander.MoveGroupCommander("scara_cpe_group")

            print "============ Robot Groups:"
            print robot.get_group_names()

            group.clear_pose_targets()

            group.set_pose_reference_frame('right')

            pose_fail1 = geometry_msgs.msg.Pose()
            pose_fail1.position.x = 0.0
            pose_fail1.position.y = 0.13
            pose_fail1.position.z = -0.025
            pose_Target_A = geometry_msgs.msg.Pose()
            pose_Target_A.position.x = -0.073
            pose_Target_A.position.y = 0.08
            pose_Target_A.position.z = -0.025

            print "============ Fail 1"

            group.set_named_target('straight')
            group.go(wait=True)
            rospy.sleep(5)

            group.set_joint_value_target(pose_fail1,True)
            group.go(wait=True)
            rospy.sleep(5)

            print "============ Fail 2"

            group.set_named_target('right')
            group.go(wait=True)
            rospy.sleep(5)

            group.set_joint_value_target(pose_Target_A,True)
            group.go(wait=True)
            rospy.sleep(5)


if __name__ == '__main__':
      moveit_test_fails()
