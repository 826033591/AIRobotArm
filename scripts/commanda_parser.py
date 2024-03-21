import mycobot_control


def execute_command(instance,command_str):
    try:
        #分割对象名和方法
        parts = command_str.split(".")
        if len(parts) != 2 or parts[0] != 'robot':
            print("Invalid command format.")
            return

        method_name = parts[1].split("()")[0] #移除括号

        #使用getattr 安全的获取方法引用
        if hasattr(instance, method_name):
            method = getattr(instance, method_name)
            method()

        else:
            print(f"the method {method_name} does not exist!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    robot = mycobot_control.MyCobotController("com4",115200)
    gpt_command = "robot.move_to_zero()"

    execute_command(robot,gpt_command)

