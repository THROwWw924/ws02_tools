/*  
  需求：订阅 laser 到 base_link 以及 camera 到 base_link 的坐标系关系，
       并生成 laser 到 camera 的坐标变换。
  步骤：
    1.包含头文件；
    2.初始化 ROS 客户端；
    3.定义节点类；
      3-1.创建tf缓存对象指针；
      3-2.创建tf监听器；
      3-3.按照条件查找符合条件的坐标系并生成变换后的坐标帧。
    4.调用 spin 函数，并传入对象指针；
    5.释放资源。
*/
// 1.包含头文件；
#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_listener.h"
#include "tf2_ros/buffer.h"
#include "tf2/LinearMath/Quaternion.h"

using namespace std::chrono_literals;

// 3.定义节点类；
class TFlisenter: public rclcpp::Node {
public:
    TFlisenter(): Node("tflisenter"){
    // 3-1.创建tf缓存对象指针；
    buffer_ = std::make_unique<tf2_ros::Buffer>(this->get_clock()); 
    lisenter_ = std::make_shared<tf2_ros::TransformListener>(*buffer_,this); 
    // 3-2.创建tf监听器；
    // 3-3.按照条件查找符合条件的坐标系并生成变换后的坐标帧。
    }
private:
    std::unique_ptr<tf2_ros::Buffer> buffer_;
    std::shared_ptr<tf2_ros::TransformListener> lisenter_;  
};

int main(int argc, char const *argv[])
{
    // 2.初始化 ROS 客户端；
    rclcpp::init(argc,argv);
    // 4.调用 spin 函数，并传入对象指针；
    rclcpp::spin(std::make_shared<TFlisenter>());
    // 5.释放资源。
    rclcpp::shutdown();
    return 0;
}

