import rclpy
from hello_interfaces.msg import MyString
from rclpy.node import Node
from pyPS4Controller.controller import Controller
import os
import subprocess
import time
os.environ['ROS_DOMAIN_ID'] = '2'

class MyController(Controller, Node):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        Node.__init__(self, 'ps4_controller_node')
        self.publisher_ = self.create_publisher(MyString, 'chatter', 1)
        self.timer = self.create_timer(1, self.timer_callback)  # 0.01秒ごとにtimer_callbackを呼び出す

    def timer_callback(self):
        # コントローラーのイベントをリッスンするためのポーリング
        self.listen(timeout=5)
        
    # id wo kimeru
    def on_share_press(self):
        subprocess.run("export ROS_DOMAIN_ID=1 && ros2 run hello talker", shell=True)
    
    def on_options_press(self):
        subprocess.run("export ROS_DOMAIN_ID=2 && ros2 run hello talker", shell=True)
            
    def on_playstation_button_press(self):
        subprocess.run("export ROS_DOMAIN_ID=3 && ros2 run hello talker", shell=True)
        
    # 箱回収の上げる方
    def on_circle_press(self):
        msg = MyString()
        msg.data = "circle"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_circle_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_triangle_press(self):
        msg = MyString()
        msg.data = "triangle"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_triangle_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_square_press(self):
        msg = MyString()
        msg.data = "square"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_square_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    # オムニ緊急停止
    def on_cross_press(self):
        msg = MyString()
        msg.data = "cross"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)


    # 箱回収の下げる方
    def on_right_arrow_press(self):
        msg = MyString()
        msg.data = "right"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)
    
    def on_right_arrow_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_up_arrow_press(self):
        msg = MyString()
        msg.data = "up"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_up_arrow_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)
        
    def on_left_arrow_press(self):
        msg = MyString()
        msg.data = "left"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_left_arrow_release(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    # 回収緊急停止
    def on_down_arrow_press(self):
        msg = MyString()
        msg.data = "release"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    # ジャンプ機構
    def on_L1_press(self):
        msg = MyString()
        msg.data = "L1ON"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_L1_release(self):
        msg = MyString()
        msg.data = "L1OFF"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_R1_press(self):
        msg = MyString()
        msg.data = "R1ON"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    def on_R1_release(self):
        msg = MyString()
        msg.data = "R1OFF"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: " + msg.data)

    # 三輪オムニの制御
    def on_R3_left(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"R3_x: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: R3_x: " + str(value))

    def on_R3_right(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"R3_x: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: R3_x: " + str(value))

    def on_R3_up(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"R3_y: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: R3_y: " + str(value))

    def on_R3_down(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"R3_y: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: R3_y: " + str(value))

    def on_L3_left(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"L3_x: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: L3_x: " + str(value))

    def on_L3_right(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"L3_x: {value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: L3_x: " + str(value))

    def on_L3_up(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"L3_y: {-value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: L3_y: " + str(-value))

    def on_L3_down(self, value):
        if -3000 < value < 3000:
            value = 0
        msg = MyString()
        msg.data = f"L3_y: {-value}"
        self.publisher_.publish(msg)
        self.get_logger().info("Published: L3_y: " + str(-value))

def main(args=None):
    rclpy.init(args=args)
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    rclpy.spin(controller)  # コントローラーとROS2ノードを同時に実行

    # コントローラが停止したら、ノードを破棄してROS通信をシャットダウンする
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
