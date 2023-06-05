'''ros2 node publishing '''
import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String

class SerialNode(Node):
    def __init__(self):
	# initializes the parent class with the provided node name
        super().__init__('serial_node')

        # instantiate serial object and assign port to it
        self.ser = serial.Serial('/dev/pts/1')

        # msg type, topic name, queue size of 10 (drop oldest if exceeded)
        self.publisher_ = self.create_publisher(String, 'air_quality', 10)

        # execute after 2s and run the callback function
        self.timer = self.create_timer(0.5, self.run_callback)


    def run_callback(self):

        # read line and prep it for publishing
        line = self.ser.readline().decode().strip()

        # log what pyserial has got to terminal
        self.get_logger().info(f'running... {line}')

        # make instantiate message object of type string
        msg = String()

        # make the data of the object equal what pyserial read
        msg.data = line

        # publish the data to our topic we made earlier
        self.publisher_.publish(msg)

def main(args=None):

    # initialise the rclpy library for use, can pass it arguments too if you wish, 
    rclpy.init(args=args)

    # instantiate node object
    serial_node = SerialNode()

    # spin the node so that the callbacks are called
    rclpy.spin(serial_node)

    # deallocate memory and remove ros2 entities made by the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()

