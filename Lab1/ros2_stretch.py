import hello_helpers.hello_misc as hm
import numpy as np

node = hm.HelloNode.quick_create('node')

try:
    #stow
    node.stow_the_robot()
    
    #move the arm and lift to maximum positions
    node.move_to_pose({'joint_arm': 0.55, 'joint_lift': 1.1}, blocking=True)

    #move the wrist to different positions, one joint at a time
    node.move_to_pose({'joint_wrist_yaw': np.radians(50)}, blocking=True)
    node.move_to_pose({'joint_wrist_pitch': np.radians(-50)}, blocking=True)
    node.move_to_pose({'joint_wrist_roll': np.radians(50)}, blocking=True)
    node.move_to_pose({'joint_gripper_finger_left': 0.165}, blocking=True)
    node.move_to_pose({'joint_gripper_finger_right': -0.35}, blocking=True)   

    #move the head
    node.move_to_pose({'joint_head_pan': np.radians(40)}, blocking=True)
    # node.move_to_pose({'joint_head_pan': node.get_joint_position('joint_head_pan') + np.radians(40)}, blocking=True)

    node.move_to_pose({'joint_head_tilt': np.radians(20)}, blocking=True)
    # node.move_to_pose({'joint_head_tilt': node.get_joint_position('joint_head_tilt') + np.radians(30)}, blocking=True)

    #stow again
    node.stow_the_robot()

    #move the robot base
    node.move_base_by(0.5, 0.0, blocking=True)
    node.rotate_base_by(np.radians(180), blocking=True)
    node.move_base_by(0.5, 0.0, blocking=True)  

finally:
    node.stop_the_robot()
    
    # Your main logic here
