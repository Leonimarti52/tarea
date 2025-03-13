import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import random

class MiPublicador(Node):
    def __init__(self):
        super().__init__('mi_publicador')
        self.publisher_ = [self.create_publisher(Bool, f'bool_array_{i}', 10) for i in range(3)]
        self.timer = self.create_timer(3, self.timer_callback)

    def timer_callback(self):
        valores = [bool(random.randint(0, 1)) for _ in range(3)]
        for i in range(3):
            msg = Bool()
            msg.data = valores[i]
            self.publisher_[i].publish(msg)
        self.get_logger().info(f'Publicando: {valores}')

def main(args=None):
    rclpy.init(args=args)
    mi_publicador = MiPublicador()
    rclpy.spin(mi_publicador)
    mi_publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
