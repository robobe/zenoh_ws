#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_system_default
from std_srvs.srv import SetBool

class DemoNode(Node):
    def __init__(self):
        super().__init__("service_demo")
        self.get_logger().info("start service demo")
        self.sub = self.create_service(SetBool, "service_demo", self.__handler, qos_profile=qos_profile_system_default)

    def __handler(self, request: SetBool.Request, response: SetBool.Response):
        self.get_logger().info(str(request.data))

        response.success = True
        response.message = "hello service response"
        return response

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