"""  
  需求：编写动态坐标变换程序，启动 turtlesim_node 以及 turtle_teleop_key 后，该程序可以发布
       乌龟坐标系到窗口坐标系的坐标变换，并且键盘控制乌龟运动时，乌龟坐标系与窗口坐标系的相对关系
       也会实时更新。

  步骤：
    1.导包；
    2.初始化 ROS 客户端；
    3.定义节点类；
      3-1.创建动态坐标变换发布方；
      3-2.创建乌龟位姿订阅方；
      3-3.根据订阅到的乌龟位姿生成坐标帧并广播。
    4.调用 spin 函数，并传入对象；
    5.释放资源。
"""
# 1.导包；
from geometry_msgs.msg import TransformStamped
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
import tf_transformations
from turtlesim.msg import Pose

#3.定义节点类
class Dynamic_tf_node(Node):
    def __init__(self):
        super().__init__("dynamic_tf_node")
        #创建动态坐标发布方
        self.tf_pub = TransformBroadcaster(self)
        #创建乌龟位姿订阅方
        self.pose_sub = self.create_subscription( 
            Pose,
            '/turtle1/pose',
            self.handle_pose,
            1)
        #根据乌龟位姿生成坐标帧并广播
    def handle_pose(self,msg):
        #组织消息
        t = TransformStamped()#创建消息对象
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle1"

        #设置相对坐标
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0

        #设置旋转，四元数欧拉角转换
        q = tf_transformations.quaternion_from_euler(0,0,msg.theta) 
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        #发布消息
        self.tf_pub.sendTransform(t)
#主函数
def main():
    # 2.初始化 ROS 客户端；
    rclpy.init()
    # 4.调用 spin 函数，并传入对象；
    node = Dynamic_tf_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    # 5.释放资源。
    rclpy.shutdown()





