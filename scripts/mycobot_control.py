from pymycobot import MyCobot
import time

class MyCobotController:

    def __init__(self, port, baud):
         self.mc = MyCobot(port, baud)
         self.speed = 80
         self.mode =0
         self.coords = []

    def grab_position(self):

        # self.mc.send_angles([4.83, 13.97, (-99.31), (-1.75), 4.39, (-0.26)], 80)
        self.mc.send_coords([149.2, (-48.3), 201.7, (-176.98), 4.55, (-84.66)], 80, 0)
        time.sleep(2)

    def move_to_zero(self):

        self.mc.send_angles([0,0,0,0,0,0],70)
        time.sleep(2)


    def gripper_open(self):

        self.mc.set_gripper_state(0,80,1)
        time.sleep(2)

    def gripper_close(self):

        self.mc.set_gripper_state(1,80,1)
        time.sleep(2)

    def grab_action(self):

        self.mc.set_gripper_state(0,80,1)
        time.sleep(3)
        self.mc.set_gripper_state(1,80,1)
        time.sleep(1)


    def plus_x_coords(self, increment):

        # x+ 前进， x- 后退
        coords = self.mc.get_coords()
        print(coords)
        if coords is None:
            print("Failed to get coordinates.")
            return  # 或者根据需要进行其他处理

        coords[0] += increment

        self.mc.send_coord(1, coords[0], self.speed)

        print(self.mc.get_coords())

    def plus_y_coords(self, increment):

        # y+ 左移， y- 右移
        coords = self.mc.get_coords()
        print(coords)
        if coords is None:
            print("Failed to get coordinates.")
            return  # 或者根据需要进行其他处理

        coords[1] += increment

        self.mc.send_coord(2, coords[1], self.speed)

        print(self.mc.get_coords())

    def plus_z_coords(self, increment):

        # z+ 抬高 ， z- 降低
        coords = self.mc.get_coords()
        print(coords)
        if coords is None:
            print("Failed to get coordinates.")
            return  # 或者根据需要进行其他处理

        coords[2] += increment

        self.mc.send_coord(3, coords[2], self.speed)

        print(self.mc.get_coords())

if __name__ == "__main__":

    robot = MyCobotController('com4', 115200)
    robot.move_to_zero()
    robot.grab_position()
    robot.plus_z_coords(10)
    time.sleep(1)
    robot.plus_x_coords(10)
    time.sleep(1)
    robot.grab_action()
