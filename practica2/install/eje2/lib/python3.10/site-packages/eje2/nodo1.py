import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
class MiPublicador(Node):
    def __init__(self):
        super().__init__('nodo1')
        self.publisher_ = self.create_publisher(Int32, 'odd', 10)
        timer_period = 0.5  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    def timer_callback(self):
        msg = Int32()
        a=random.randint(0,10)
        msg.data =a
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        self.i += 1
def main(args=None):
    rclpy.init(args=args)
    mi_publicador = MiPublicador()
    rclpy.spin(mi_publicador)
    mi_publicador.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()