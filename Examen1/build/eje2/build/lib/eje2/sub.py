import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray  # Cambiar a Float32MultiArray para recibir múltiples promedios

class MiListener(Node):
    def __init__(self):
        super().__init__('Nodo5')
        # Suscribirse al canal 'sum4' que publica un mensaje Float32MultiArray
        self.subscription = self.create_subscription(Float32MultiArray, 'filtered_sensor', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        # Incrementar el contador
        self.i += 1
        
        # Acceder a los tres promedios enviados
        pro_1, pro_2, pro_3 = msg.data
        
        # Mostrar los promedios recibidos
        self.get_logger().info(f'Recibido: Promedio 1: "{pro_1}", Promedio 2: "{pro_2}", Promedio 3: "{pro_3}"')

def main(args=None):
    rclpy.init(args=args)
    mi_listener = MiListener()
    rclpy.spin(mi_listener)
    mi_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
