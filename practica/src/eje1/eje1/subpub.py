import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8,Int32
class MiListener(Node):
    def __init__(self):
        self.sum=0
        self.i=0
        super().__init__('mi_listener')
        self.subscription = self.create_subscription(Int8,'numbers',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Int32, 'sum', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
    def timer_callback(self):
        msg = Int32()
        msg.data =self.sum
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        self.i += 1
    def listener_callback(self, msg):
        self.sum=msg.data+self.sum
        self.get_logger().info(f'Recibido: "{msg.data}", Suma: "{self.sum}"')


def main(args=None):
    rclpy.init(args=args)
    mi_listener = MiListener()
    rclpy.spin(mi_listener)
    mi_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()