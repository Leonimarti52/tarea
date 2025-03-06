import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MiListener(Node):
    def __init__(self):
        super().__init__('nodo3')
        
        # Suscriptores a los tópicos "even" y "odd"
        self.subscription_even = self.create_subscription(
            Int32, 'even', self.listener_callback, 10)
        self.subscription_odd = self.create_subscription(
            Int32, 'odd', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    mi_listener = MiListener()
    rclpy.spin(mi_listener)
    mi_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
