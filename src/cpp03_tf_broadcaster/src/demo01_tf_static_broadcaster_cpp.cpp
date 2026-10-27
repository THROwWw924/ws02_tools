/*
需求：自实现静态坐标变换广播器，执行该程序时，需要传入参数
  ros2 run 包名 可执行程序 位移量 x y z roll pitch yaw frame child_frame
流程;
  判断传入的参数是否合法
  自定义节点类：
    1.创建一个广播对象
    2.组织并发布数据
    3.
*/
#include <geometry_msgs/msg/transform_stamped.hpp>

#include <rclcpp/rclcpp.hpp>
#include <tf2/LinearMath/Quaternion.h>//将欧拉角转换为四元数
#include <tf2_ros/static_transform_broadcaster.h>

using std::placeholders::_1;

class TFStaticBroadcaster : public rclcpp::Node
{
public:
 TFStaticBroadcaster(char *argv[]) : Node("tfstaticbroadcaster")
  {
    // 在这里编写节点初始化代码
    //3-1创建节点对象
    //tf2_ros::StaticTransformBroadcaster
    Broadcaster_ = std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);
    //3-2组织发布数据
    pub_static_tf(argv);

  }

private:
  // 在这里声明成员变量
  std::shared_ptr<tf2_ros::StaticTransformBroadcaster> Broadcaster_;
  void pub_static_tf(char *argv[]){
    //组织消息
    geometry_msgs::msg::TransformStamped transform;//这是一个消息对象
    //设置时间戳
    transform.header.stamp = this->now();
    //父级坐标系，已经封装在argv中了
    transform.header.frame_id = argv[7];
    transform.child_frame_id = argv[8];//子级坐标系
    //设置平移量
    transform.transform.translation.x = atof(argv[1]);
    transform.transform.translation.y = atof(argv[2]);
    transform.transform.translation.z = atof(argv[3]);
    //设置欧拉角（四元数）
    //将欧拉角转换成四元数
    tf2::Quaternion qtn;
    qtn.setRPY(atof(argv[4]),atof(argv[5]),atof(argv[6]));
    transform.transform.rotation.x = qtn.x();
    transform.transform.rotation.y = qtn.y();
    transform.transform.rotation.z = qtn.z();
    transform.transform.rotation.w = qtn.w();
    //发布
    Broadcaster_->sendTransform(transform);
  }
};  

int main(int argc, char *argv[])
{
  //判断传入的参数是否合法；
  if(argc != 9){
    RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),"传入的参数不合法");
    return 1;
  }
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared <TFStaticBroadcaster>(argv));
  rclcpp::shutdown();
  return 0;
}
