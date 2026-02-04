import stretch_body.robot
import numpy as np

robot = stretch_body.robot.Robot()
robot.startup()

#stow the robot
robot.stow()
# robot.push_command()

#move the arm and lift to max positions
robot.arm.move_to(0.55)
robot.lift.move_to(1.1)
robot.push_command()
robot.wait_command() #try it may not work

#From docs:
"""The gripper uses the same move_to(name, pos) API, 
and accepts values between -100 to 100, where the gripper 
is fully closed at -100 and fully open at 100."""
#move the wrist to different positions, one joint at a time

robot.end_of_arm.move_to('wrist_yaw', 50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('wrist_pitch', -50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('wrist_roll', 50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('stretch_gripper',50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('stretch_gripper',-50)
robot.push_command()
robot.wait_command()

#move the head
robot.head.move_by('head_pan', np.radians(40)) 
robot.push_command()
robot.wait_command()
robot.head.move_by('head_tilt', np.radians(30)) 
robot.push_command()
robot.wait_command()

#stow the robot again
robot.stow()
robot.push_command()
robot.wait_command()

#move the robot base
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()
robot.base.rotate_by(np.radians(180))
robot.push_command()
robot.wait_command()
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()