#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_system_default
from std_msgs.msg import String

class DemoNode(Node):
    def __init__(self):
        super().__init__("sub_demo")
        self.get_logger().info("start sub demo")
        self.sub = self.create_subscription(String, "string_demo", self.__handler, qos_profile=qos_profile_system_default)

    def __handler(self, msg: String):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = DemoNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


"""
ros2 topic pub -r 1 /string_demo std_msgs/msg/String "{data: 'hello world'}"
"""