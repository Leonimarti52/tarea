import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
class MiListener(Node):
    def __init__(self):
        super().__init__('mi_listener')
        self.subscription = self.create_subscription(Int32,'sum',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        self.i=0
    def listener_callback(self, msg):
        self.i+=1
        self.pro=msg.data/self.i
        self.get_logger().info(f'Recibido: "{msg.data}" Promedio: "{self.pro}"')
def main(args=None):
    rclpy.init(args=args)
    mi_listener = MiListener()
    rclpy.spin(mi_listener)
    mi_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()