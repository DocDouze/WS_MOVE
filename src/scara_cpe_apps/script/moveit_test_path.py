#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import geometry_msgs.msg


class moveit_test_named_target:


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

            group.set_pose_reference_frame('base_link')

            pose_target_B = geometry_msgs.msg.Pose()
            pose_target_B.position.x = 0.035
            pose_target_B.position.y = 0.14
            pose_target_B.position.z = -0.025
            pose_target_D = geometry_msgs.msg.Pose()
            pose_target_D.position.x = -0.044
            pose_target_D.position.y = 0.08
            pose_target_D.position.z = -0.025

            group.set_named_target('straight')
            group.go(wait=True)
            rospy.sleep(5)

            waypoints = []
            while not rospy.is_shutdown():
                point_initial = group.get_current_pose().pose
                point_initial.position.z = -0.025
                waypoints.append(copy.deepcopy(point_initial))
                waypoints.append(copy.deepcopy(pose_target_B))
                waypoints.append(copy.deepcopy(pose_target_D))
                (plan3, fraction) = group.compute_cartesian_path(
                                 waypoints,   # waypoints to follow
                                 0.001,        # eef_step
                                 0.0)         # jump_threshold
                group.execute(plan3)
                rospy.sleep(5)
                point_initial = group.get_current_pose().pose
                point_initial.position.z = -0.025
                waypoints.append(copy.deepcopy(point_initial))
                waypoints.append(copy.deepcopy(pose_target_D))
                waypoints.append(copy.deepcopy(pose_target_B))
                (plan3, fraction) = group.compute_cartesian_path(
                                 waypoints,   # waypoints to follow
                                 0.001,        # eef_step
                                 0.0)         # jump_threshold
                group.execute(plan3)
                rospy.sleep(5)


if __name__ == '__main__':
      moveit_test_named_target()
