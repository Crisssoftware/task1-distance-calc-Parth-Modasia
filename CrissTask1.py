import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('distance_calculator')
        # Subscriber to /turtle1/pose
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.subscription  # Prevent unused variable warning

        # Publisher to /turtle1/distance_from_origin
        self.publisher = self.create_publisher(
            Float32,
            '/turtle1/distance_from_origin',
            10)

    def pose_callback(self, msg):
        # Extract x and y from the Pose message
        x = msg.x
        y = msg.y

        # Compute distance from origin
        distance = math.sqrt(x**2 + y**2)

        # Log the computed distance
        self.get_logger().info(f'Distance from origin: {distance:.2f}')

        # Publish the distance
        distance_msg = Float32()
        distance_msg.data = distance
        self.publisher.publish(distance_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
