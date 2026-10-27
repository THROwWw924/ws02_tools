"""  
    需求：编写静态坐标变换程序，执行时传入两个坐标系的相对位姿关系以及父子级坐标系id，
         程序运行发布静态坐标变换。
    步骤：
        1.导包；
        2.判断终端传入的参数是否合法；
        3.初始化 ROS 客户端；
        4.定义节点类；
            4-1.创建静态坐标变换发布方；
            4-2.组织并发布消息。
        5.调用 spin 函数，并传入对象；
        6.释放资源。 

"""
# 1.导包；
import sys
from geometry_msgs.msg import TransformStamped
import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import tf_transformations

# 4.定义节点类；
class MinimalStaticFrameBroadcasterPy(Node):

    def __init__(self):
        super().__init__('minimal_static_frame_broadcaster_py')
        # 4-1.创建静态坐标变换发布方；
        self._tf_publisher = StaticTransformBroadcaster(self)
        self.make_transforms()

    # 4-2.组织并发布消息。
    def make_transforms(self):
        # 组织消息
        static_transformStamped = TransformStamped()
        static_transformStamped.header.stamp = self.get_clock().now().to_msg()
        static_transformStamped.header.frame_id = sys.argv[7]
        static_transformStamped.child_frame_id = sys.argv[8]
        static_transformStamped.transform.translation.x = float(sys.argv[1])
        static_transformStamped.transform.translation.y = float(sys.argv[2])
        static_transformStamped.transform.translation.z = float(sys.argv[3])
        quat = tf_transformations.quaternion_from_euler(
            float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))
        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]
        # 发布消息
        self._tf_publisher.sendTransform(static_transformStamped)


def main():
    # 2.判断终端传入的参数是否合法；
    logger = rclpy.logging.get_logger('logger')
    if len(sys.argv) < 9:
        logger.info('运行程序时请按照：x y z roll pitch yaw frame_id child_frame_id 的格式传入参数')
        sys.exit(0)

    # 3.初始化 ROS 客户端；
    rclpy.init()
    # 5.调用 spin 函数，并传入对象；
    node = MinimalStaticFrameBroadcasterPy()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # 6.释放资源。 
    rclpy.shutdown()