import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class SelfDrive(Node):
    

        if 0.01 < scan.ranges[0] <= 0.25 or 0.01 < scan.ranges[20] <= 0.25:
            twist.linear.x = 0.0
            twist.angular.z = -1.5
            self.get_logger().info(f"scan: {scan.ranges[30]}, right")


        elif 0.01 < scan.ranges[70] <= 0.20 :
            twist.linear.x = 0.15
            twist.angular.z = -0.0001
            self.get_logger().info(f"scan: {scan.ranges[90]}, sright")

        elif 0.01 < scan.ranges[90] <= 0.20:
            twist.linear.x = 0.00
            twist.angular.z = 1.3
            self.get_logger().info(f"scan: {scan.ranges[120]}, left")


        self.pub_velo.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = SelfDrive()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
