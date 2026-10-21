from launch import LaunchDescription
from launch_ros.actions import Node
# 封装终端指令相关类--------------
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取-----------------
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import LaunchConfiguration
# 文件包含相关-------------------
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# 分组相关----------------------
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# 事件相关----------------------
# from launch.event_handlers import OnProcessStart, OnProcessExit
# from launch.actions import ExecuteProcess, RegisterEventHandler,LogInfo
# 获取功能包下share目录路径-------
from ament_index_python.packages import get_package_share_directory
import os
"""
    需求：演示node的使用。

    构造函数参数说明：
    :param: executable 可执行程序
            :param: package 被执行的程序所属的功能包
            :param: name the :name of the node
            :param: namespace :the ROS namespace for this Node
            :param: exec_name :the label used to represent the process.
                Defaults to the basename of node executable.
            :param: parameters list of names of yaml files with parameter rules,
                or dictionaries of parameters.
            :param: remappings ordered list of 'to' and 'from' string pairs to be
                passed to the node as ROS remapping rules:实现话题重映射！！！
            :param: ros_arguments list of ROS arguments for the node：为节点传参
                --ros-args remap
            :param: arguments list of extra arguments for the node：为节点传参
                xx yy zz --ros-args
"""
def generate_launch_description():
    # turtle1 = Node(
    #     package="turtlesim",
    #     executable="turtlesim_node",
    #     exec_name="my_label",
    #     ros_arguments=["--remap","__ns:=/t2"]
    #     #等价于ros2 run turtlesim turtlesim_node --ros-args --remap __ns:=/t1
    #     )
    turtle2 = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="haha",
        #传入参数，修改参数
        #方式1
        #parameters=[{"background_r":255,"background_g":0,"background_b":0}]
        #方式2（更常用）：把参数保存在yaml文件之中,读取yaml文件。通过yaml文件的绝对路径的来读取，读install上的，不读src（源代码，读不到）
        #parameters=["/home/derrickrose/ws02_tools/src/cpp01_launch/config/haha.yaml"]#绝对路径，不推荐
        #动态获取路径
        parameters=[os.path.join(get_package_share_directory("cpp01_launch"),"config","haha.yaml")]
    )
    return LaunchDescription([turtle2])