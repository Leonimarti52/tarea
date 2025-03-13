import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class MiSubscriptor(Node):
    def __init__(self):
        super().__init__('mi_subscriptor')
        self.valores = [None] * 3  # Lista para almacenar los valores recibidos
        # Crear las suscripciones correctamente
        self.subscripciones = [
            self.create_subscription(Bool, f'bool_array_{i}', self.listener_callback(i), 10)
            for i in range(3)
        ]
        self.i = 0

    def listener_callback(self, index):
        def callback(msg):
            self.valores[index] = msg.data
            self.i += 1
            if self.i % 3 == 0:
                accion = obtener_accion(*self.valores)
                self.get_logger().info(f'Acción: {accion}')
        return callback

def obtener_accion(SI, SC, SD):
    # Diccionario para mapear las combinaciones de sensores a acciones
    combinaciones_acciones = {
        (0, 0, 0): "1 1 Adelante",
        (0, 0, 1): "0 1 Derecha",
        (0, 1, 0): "0 0 Alto",
        (0, 1, 1): "0 1 Derecha",
        (1, 0, 0): "1 0 Izquierda",
        (1, 0, 1): "1 1 Adelante",
        (1, 1, 0): "1 0 Izquierda",
        (1, 1, 1): "0 0 Alto"
    }
    # Obtenemos la acción asociada con la combinación de sensores
    accion = combinaciones_acciones.get((SI, SC, SD), "Estado desconocido")
    return accion

def main(args=None):
    rclpy.init(args=args)
    mi_subscriptor = MiSubscriptor()
    rclpy.spin(mi_subscriptor)
    mi_subscriptor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
