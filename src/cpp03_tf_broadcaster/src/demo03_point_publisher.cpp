/*  
    需求：发布雷达坐标系中某个坐标点相对于雷达（laser）坐标系的位姿。
    步骤：
        1.包含头文件；
        2.初始化 ROS 客户端；
        3.定义节点类；
            3-1.创建坐标点发布方；
            3-2.创建定时器；
            3-3.组织并发布坐标点消息。
        4.调用 spin 函数，并传入对象指针；
        5.释放资源。


*/
// 1.包含头文件；
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/point_stamped.hpp"

using namespace std::chrono_literals;
// 3.定义节点类
class demo03_point_publisher:public rclcpp::Node
{
private:
    rclcpp::Publisher<geometry_msgs::msg::PointStamped>::SharedPtr point_pub;
    rclcpp::TimerBase::SharedPtr timer_;
    double_t x;
    void on_timer(){
        //组织消息并发布
        geometry_msgs::msg::PointStamped point;
        point.header.frame_id = "laser";
        point.header.stamp = this->now();
        x += 0.03;
        point.point.x = x;
        point.point.y = 0.0;
        point.point.z = 0.1;
        point_pub->publish(point);
    }
public:
    demo03_point_publisher():Node("point_publisher"),x(0.0){
        //创建坐标发布方
        point_pub = this->create_publisher<geometry_msgs::msg::PointStamped>("point",10);
        timer_ =this->create_wall_timer(0.1s,std::bind(&demo03_point_publisher::on_timer,this));
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<demo03_point_publisher>());
    rclcpp::shutdown();
    return 0;
}

