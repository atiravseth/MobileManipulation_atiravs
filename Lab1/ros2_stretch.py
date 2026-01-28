import hello_helpers.hello_misc as hm
import numpy as np

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)
        # my_node's main logic goes here

        #stow the robot
        hm.stow_the_robot() 

        #move the arm and lift to maximum positions
        hm.move_to_pose({'joint_arm': 0.55, 'joint_lift': 1.1}, blocking=True)

        #move the wrist to different positions, one joint at a time
        hm.move_to_pose({'joint_wrist_yaw': np.radians(50)}, blocking=True)
        hm.move_to_pose({'joint_wrist_pitch': np.radians(-50)}, blocking=True)
        hm.move_to_pose({'joint_wrist_roll': np.radians(50)}, blocking=True)
        hm.move_to_pose({'joint_gripper_finger_left': 50}, blocking=True)
        hm.move_to_pose({'joint_gripper_finger_right': -50}, blocking=True)

        #move the head
        hm.move_to_pose({'joint_head_pan': hm.get_joint_position('joint_head_pan') + np.radians(40)}, blocking=True)
        hm.move_to_pose({'joint_head_tilt': hm.get_joint_position('joint_head_tilt') + np.radians(30)}, blocking=True)  

        #stow the robot again
        hm.stow_the_robot()

        #move the robot base
        hm.move_base_by(0.5, 0.0, blocking=True)
        hm.rotate_base_by(np.radians(180), blocking=True)
        hm.move_base_by(0.5, 0.0, blocking=True)

node = MyNode()
node.main()

