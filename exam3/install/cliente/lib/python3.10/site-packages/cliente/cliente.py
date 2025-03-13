import rclpy
from rclpy.node import Node
from interface.srv import Angle
import numpy as np

class ClienteCinematica(Node):
    def __init__(self):
        super().__init__('cliente_cinematica')
        self.cli = self.create_client(Angle, '/calcular_cinematica')
        
        while not self.cli.wait_for_service(timeout_sec=3.0):
            self.get_logger().info('Esperando servicio /calcular_cinematica...')
        
        self.enviar_angulos()

    def enviar_angulos(self):
        configuraciones = [
            [0, 0, 0],          # Configuración 1
            [20, 45, 10],       # Configuración 2
            [10, -30, 25]       # Configuración 3
        ]

        resultados = []  # Para almacenar las respuestas
        
        for i, config in enumerate(configuraciones):
            request = Angle.Request()
            request.theta1 = float(config[0])
            request.theta2 = float(config[1])
            request.theta3 = float(config[2])
            request.theta4 = 0.0  # Se deja en 0 si no se usa

            self.get_logger().info(f'📤 Enviando Configuración {i+1}: {config} grados')
            
            future = self.cli.call_async(request)
            rclpy.spin_until_future_complete(self, future)
            
            if future.result():
                respuesta = future.result()
                resultados.append([respuesta.x, respuesta.y, respuesta.z, respuesta.roll, respuesta.pitch, respuesta.yaw])
                self.get_logger().info(f'✅ Respuesta: {respuesta}')
            else:
                self.get_logger().error('❌ Error al llamar al servicio')

        self.get_logger().info(f'📊 Resultados almacenados: {resultados}')

def main():
    rclpy.init()
    cliente = ClienteCinematica()
    cliente.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()