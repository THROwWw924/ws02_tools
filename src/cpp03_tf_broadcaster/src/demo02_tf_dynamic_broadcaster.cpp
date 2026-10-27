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

class TF_dynamic_node : public rclcpp::Node
{
public:
  TF_dynamic_node() : Node("tf_dynamic_node")
  {
    // 1.创建动态广播器
    broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(this);
    // 2.创建一个乌龟位姿订阅方
    Pose_sub = this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose",10,std::bind(&TF_dynamic_node::do_pose,this,std::placeholders::_1))
    // 3.回调函数中，获取乌龟位姿，并生成相对关系并发布
  }

private:
  // 在这里声明成员变量
  std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster_;
  rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr Pose_sub;
  void do_pose(const turtlesim::msg::Pose & pose){
    
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TF_dynamic_node>());
  rclcpp::shutdown();
  return 0;
}