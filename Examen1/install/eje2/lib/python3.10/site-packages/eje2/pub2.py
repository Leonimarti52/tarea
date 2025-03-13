import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class MiPublicador(Node):
    def __init__(self):
        super().__init__('Nodo2')
        self.publisher_ = self.create_publisher(Float32, 'Sensor_2', 10)
        timer_period = 0.5  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        a = float(random.randint(0, 10))  # Convertir el número aleatorio a float
        msg.data = a
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    mi_publicador = MiPublicador()
    rclpy.spin(mi_publicador)
    mi_publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
