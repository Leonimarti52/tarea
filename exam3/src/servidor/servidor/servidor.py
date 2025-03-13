import rclpy
from rclpy.node import Node
from interface.srv import Angle
import numpy as np
class ServidorCinematica(Node):
    def __init__(self):
        super().__init__('servidor_cinematica')
        self.srv = self.create_service(Angle, '/calcu', self.callback_cinematica)
    def callback_cinematica(self, request, response):
        theta1 = np.deg2rad(request.theta1)
        theta2 = np.deg2rad(request.theta2)
        theta3 = np.deg2rad(request.theta3)
        theta4 = np.deg2rad(request.theta4)
        L1 = 69.5 / 1000  
        L2 = 71.5 / 1000  
        R_x = np.array([[1, 0, 0], [0, np.cos(theta1), -np.sin(theta1)], [0, np.sin(theta1), np.cos(theta1)]])
        R_y1 = np.array([[np.cos(theta2), 0, np.sin(theta2)], [0, 1, 0], [-np.sin(theta2), 0, np.cos(theta2)]])
        R_y2 = np.array([[np.cos(theta3), 0, np.sin(theta3)], [0, 1, 0], [-np.sin(theta3), 0, np.cos(theta3)]])
        R_y3 = np.array([[np.cos(theta4), 0, np.sin(theta4)], [0, 1, 0], [-np.sin(theta4), 0, np.cos(theta4)]])
        T_z1 = np.array([[1, 0, 0, 0], [0, 1, 0, -L1], [0, 0, 1, 0], [0, 0, 0, 1]])
        T_z2 = np.array([[1, 0, 0, 0], [0, 1, 0, -L2], [0, 0, 1, 0], [0, 0, 0, 1]])
        R_x_4x4 = np.eye(4)
        R_x_4x4[:3, :3] = R_x
        R_y1_4x4 = np.eye(4)
        R_y1_4x4[:3, :3] = R_y1
        R_y2_4x4 = np.eye(4)
        R_y2_4x4[:3, :3] = R_y2
        R_y3_4x4 = np.eye(4)
        R_y3_4x4[:3, :3] = R_y3
        M = np.dot(R_x_4x4, np.dot(R_y1_4x4, np.dot(T_z1, np.dot(R_y2_4x4, np.dot(T_z2, R_y3_4x4)))))
        response.x = M[0, 3]
        response.y = M[1, 3]
        response.z = M[2, 3]
        response.roll = np.rad2deg(np.arctan2(M[2, 1], M[2, 2]))
        response.pitch = np.rad2deg(np.arctan2(-M[2, 0], np.sqrt(M[2, 1]**2 + M[2, 2]**2)))
        response.yaw = np.rad2deg(np.arctan2(M[1, 0], M[0, 0]))
        self.get_logger().info(f'Respuesta calculada: x={response.x}, y={response.y}, z={response.z}, roll={response.roll}, pitch={response.pitch}, yaw={response.yaw}')
        return response
def main():
    rclpy.init()
    servidor = ServidorCinematica()
    rclpy.spin(servidor)
    servidor.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()