#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_system_default
from std_msgs.msg import String

class DemoNode(Node):
    def __init__(self):
        super().__init__("pub_demo")
        self.get_logger().info("start pub demo")
        self.pub = self.create_publisher(String, "pub_string", qos_profile=qos_profile_system_default)
        self.timer = self.create_timer(1.0, self.__handler)
        self.counter = 0

    def __handler(self):
        self.counter += 1
        msg = String()
        msg.data = f"hello: {self.counter}"
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DemoNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()