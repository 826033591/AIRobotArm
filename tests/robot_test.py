from pymycobot.mycobot import MyCobot
import time
mc =MyCobot('com4', 115200)

mc.send_angles([0, 0, 0, 0, 0, 0], 70)
time.sleep(2)
mc.send_coords([149.2, (-48.3), 201.7, (-176.98), 4.55, (-84.66)], 80, 0)


def plus_x_coords(self, increment):
    coords = self.mc.get_coords()
    print(coords)
    if coords is None:
        print("Failed to get coordinates.")
        return  # 或者根据需要进行其他处理

    coords[0] += increment

    self.mc.send_coord(1, increment, self.speed)

# increment = 20
# coords = mc.get_coords()
#
# print(coords)
# coords[0] += increment
# mc.send_coord(1, increment, 80)
time.sleep(2)
mc.send_coord(1,100,80)