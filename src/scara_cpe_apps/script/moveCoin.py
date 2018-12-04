#! /usr/bin/env python


import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from std_msgs.msg import Bool


class moveCoin:


    def __init__(self):

        self.detect_metal = False
        self.grip = Bool()

        print "============ Starting tutorial setup"
        moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node('move_group_python_interface_tutorial',anonymous=True)

        robot = moveit_commander.RobotCommander()

        group = moveit_commander.MoveGroupCommander("scara_cpe_group")

        grip_pub = rospy.Publisher('/grip',Bool,queue_size=10)

        rospy.Subscriber('/detect_metal', Bool,self.detect_callback)

        print "============ Robot Groups:"
        print robot.get_group_names()

        group.clear_pose_targets()

        group.set_pose_reference_frame('base_link')
        pose_Target_A = geometry_msgs.msg.Pose()
        pose_Target_A.position.x = -0.073
        pose_Target_A.position.y = 0.08
        pose_Target_A.position.z = -0.025

        pose_target_B = geometry_msgs.msg.Pose()
        pose_target_B.position.x = 0.035
        pose_target_B.position.y = 0.14
        pose_target_B.position.z = -0.025

        group.set_joint_value_target(pose_Target_A, True)
        group.go(wait=True)
        rospy.sleep(1)

        if self.detect_metal:
            self.grip = True
            grip_pub.publish(self.grip)

        rospy.sleep(5)

        group.set_joint_value_target(pose_target_B, True)
        group.go(wait=True)
        rospy.sleep(1)

        self.grip = False
        grip_pub.publish(self.grip)

        rospy.sleep(5)

        group.set_named_target('straight')
        group.go(wait=True)

    def detect_callback(self, data):
        self.detect_metal = data.data
        if data.data:
            rospy.loginfo("Piece detecte\n")



if __name__ == '__main__':
    moveCoin()