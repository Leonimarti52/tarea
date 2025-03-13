import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray  # Usamos Float32MultiArray para publicar múltiples promedios

class MiListener(Node):
    def __init__(self):
        super().__init__('Nodo4')
        # Crear 3 suscripciones a diferentes temas
        self.subscription_1 = self.create_subscription(Float32, 'Sensor_1', self.listener_callback_1, 10)
        self.subscription_2 = self.create_subscription(Float32, 'Sensor_2', self.listener_callback_2, 10)
        self.subscription_3 = self.create_subscription(Float32, 'Sensor_3', self.listener_callback_3, 10)
        
        self.subscription_1  # prevent unused variable warning
        self.subscription_2  # prevent unused variable warning
        self.subscription_3  # prevent unused variable warning
        
        self.i_1 = 0
        self.i_2 = 0
        self.i_3 = 0
        self.pro_1 = 0.0
        self.pro_2 = 0.0
        self.pro_3 = 0.0
        
        # Crear un publicador para publicar los 3 promedios en un único canal
        self.publisher_ = self.create_publisher(Float32MultiArray, 'filtered_sensor', 10)
        
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback_1(self, msg):
        self.i_1 += 1
        self.pro_1 = float(msg.data) / self.i_1  # Asegurarse de que sea un float
        self.get_logger().info(f'Recibido de sum_1: "{msg.data}" Promedio_1: "{self.pro_1}"')

    def listener_callback_2(self, msg):
        self.i_2 += 1
        self.pro_2 = float(msg.data) / self.i_2  # Asegurarse de que sea un float
        self.get_logger().info(f'Recibido de sum_2: "{msg.data}" Promedio_2: "{self.pro_2}"')

    def listener_callback_3(self, msg):
        self.i_3 += 1
        self.pro_3 = float(msg.data) / self.i_3  # Asegurarse de que sea un float
        self.get_logger().info(f'Recibido de sum_3: "{msg.data}" Promedio_3: "{self.pro_3}"')

    def timer_callback(self):
        # Crear el mensaje de tipo Float32MultiArray con los 3 promedios
        msg = Float32MultiArray()
        
        # Asegurarse de que los promedios sean de tipo float
        msg.data = [float(self.pro_1), float(self.pro_2), float(self.pro_3)]
        
        # Publicar el mensaje
        self.publisher_.publish(msg)

        # Log para saber que se ha publicado
        self.get_logger().info(f'Publicando: Promedio 1: {self.pro_1}, Promedio 2: {self.pro_2}, Promedio 3: {self.pro_3}')

def main(args=None):
    rclpy.init(args=args)
    mi_listener = MiListener()
    rclpy.spin(mi_listener)
    mi_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
