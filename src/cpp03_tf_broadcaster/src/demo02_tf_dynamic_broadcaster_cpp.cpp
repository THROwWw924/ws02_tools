/*
    需求：启动turtlesim_node节点，编写程序，发布乌龟（turtle1）相对于框体(world)的一个位姿
    实现流程：
        自定义节点类：
            1.创建动态广播器
            2.创建一个乌龟位姿订阅方
            3.回调函数中，获取乌龟位姿，并生成相对关系并发布
*/
#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "turtlesim/msg/pose.hpp"
#include "geometry_msgs/msg/transform_stamped.hpp"  
#include "tf2/LinearMath/Quaternion.h"

class TF_dynamic_node : public rclcpp::Node
{
public:
  TF_dynamic_node() : Node("tf_dynamic_node")
  {
    // 1.创建动态广播器
    broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(this);
    // 2.创建一个乌龟位姿订阅方
    Pose_sub = this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose",10,std::bind(&TF_dynamic_node::do_pose,this,std::placeholders::_1));
    // 3.回调函数中，获取乌龟位姿，并生成相对关系并发布
  }

private:
  // 在这里声明成员变量
  std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster_;
  rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr Pose_sub;
  void do_pose(const turtlesim::msg::Pose & pose){
    //组织消息
    geometry_msgs::msg::TransformStamped ts;
    ts.header.stamp = this->now();
    ts.header.frame_id = "world";
    ts.child_frame_id = "turtle1";
    ts.transform.translation.x = pose.x;
    ts.transform.translation.y = pose.y;
    ts.transform.translation.z = 0.0;
    //欧拉角转换出四元数
    //乌龟的欧拉角只有yaw上的取值，row = 0,pitch =0
    tf2::Quaternion qtn;
    qtn.setRPY(0,0,pose.theta);
    ts.transform.rotation.x = qtn.x();
    ts.transform.rotation.y = qtn.y();
    ts.transform.rotation.z = qtn.z();
    ts.transform.rotation.w = qtn.w();

    //发布
    broadcaster_->sendTransform(ts);
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TF_dynamic_node>());
  rclcpp::shutdown();
  return 0;
}