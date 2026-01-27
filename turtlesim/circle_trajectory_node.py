#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleTrajectoryNode(Node):

    def __init__(self):

        super().__init__("circle_trajectory_node")
        self.cmd_vel_publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_timer(1.0, self.circle_callback)

    def circle_callback(self):

        msg = Twist()

        msg.linear.x = 0.5
        msg.angular.z = 5.0

        self.cmd_vel_publisher.publish(msg)

def main(args=None):

    rclpy.init(args=args)
    node = CircleTrajectoryNode()
    rclpy.spin(node)
    rclpy.shutdown()