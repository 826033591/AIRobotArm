pre_training= "Generate Python code that matches the following requirements: " \
               "\nUse an instance of the MyCobotController class robot to perform a specific action." \
               " The instance already contains methods such as move_to_zero() to return to the initial position, " \
               "grab_position() to move to the grab position, and plus_x_coords(value), plus_y_coords(value), " \
               "plus_z_coords(value) to move specific distances on the X, Y, and Z axes. \nYou don’t need to output other textual content," \
               " just output the code directly, for example, the robot arm returns to the origin.robot.move_to_zero()\nThe requirements are as follows:" \
               "Let the robotic arm return to the origin.Move to grab position.Increase the Z-axis of the robot arm by 30"

OPENAI_API_KEY = "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"

SPEECH_RECOGNITION_LANGUAGE = "en-US"

ROBOT_ARM_CONNECTION = ("com4",115200)

# 日志配置
LOGGING = {
    'level': 'INFO',  # 日志级别
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志格式
    'datefmt': '%Y-%m-%d %H:%M:%S',  # 时间格式
    'filename': 'logs/app.log',  # 日志文件路径
    'filemode': 'a',  # 文件模式，'a'代表追加，'w'代表覆盖
}

