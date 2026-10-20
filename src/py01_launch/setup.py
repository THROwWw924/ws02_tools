from setuptools import find_packages, setup

package_name = 'py01_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #launch文件相关配置
        ('share/' + package_name, ['launch/py/py01_helloworld_launch.py']),
        ('share/' + package_name, ['launch/xml/xml01_helloworld_launch.xml']),
        ('share/' + package_name, ['launch/yaml/yaml01_helloworld_launch.yaml']),
         
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='derrickrose',
    maintainer_email='2944223027@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
