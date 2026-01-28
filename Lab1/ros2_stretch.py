import hello_helpers.hello_misc as hm

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)
        # my_node's main logic goes here
        hm.move_to_pose({'joint_arm': 0.7}, blocking=True)

node = MyNode()
node.main()

####
node.stow_the_robot() 
node.move_to_pose({'joint_arm': 0.7}, blocking=True) 
node.move_to_pose({‘joint_wrist_yaw': 
           node.joint_state.position[node.joint_state.name.index(‘joint_wrist_yaw')] +  
           np.radians(45)}, blocking=True)
