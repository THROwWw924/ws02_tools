"""  
    需求：发布雷达坐标系中某个坐标点相对于雷达（laser）坐标系的位姿。
    步骤：
        1.导包；
        2.初始化 ROS 客户端；
        3.定义节点类；
            3-1.创建坐标点发布方；
            3-2.创建定时器；
            3-3.组织并发布坐标点消息。
        4.调用 spin 函数，并传入对象；
        5.释放资源。
"""
# 1.导包；
from geometry_msgs.msg import PointStamped
import rclpy
from rclpy.node import Node

# 3.定义节点类
class Point_pub(Node):
    def __init__(self):
        super().__init__("point_pub")
        #3-1 创建坐标点发布方
        self.point_pub = self.create_publisher(PointStamped,"point",10)
        #3-2 
        self.timer = self.create_timer(1.0,self.on_timer)
        self.x = 0
    def on_timer(self):
        #3-3 组织消息并发布
        ps = PointStamped()
        ps = PointStamped()
        ps.header.stamp = self.get_clock().now().to_msg()
        ps.header.frame_id = 'laser'
        self.x += 0.02
        ps.point.x = self.x
        ps.point.y = 0.0
        ps.point.z = 0.2
        self.point_pub.publish(ps)
def main():
    # 2.初始化 ROS 客户端；
    rclpy.init()
    # 4.调用 spin 函数，并传入对象；
    node = Point_pub()
    rclpy.spin(node)
    # 5.释放资源。3-3.组织并发布坐标点消息。