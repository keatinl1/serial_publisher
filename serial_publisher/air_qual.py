'''ros2 node publishing '''
import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String

class SerialNode(Node):
    def __init__(self):
        super().__init__('serial_node')

        self.ser = serial.Serial('/dev/pts/1')
        self.publisher_ = self.create_publisher(String, 'air_quality', 10)

    def run(self):

        while rclpy.ok():

            line = self.ser.readline().decode().strip()

            self.get_logger().info(f'running... {line}')

            msg = String()
            msg.data = line
            self.publisher_.publish(msg)

    def close(self):
        self.ser.close()

def main(args=None):
    rclpy.init(args=args)
    serial_node = SerialNode()

    try:
        serial_node.run()
    finally:
        serial_node.close()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

