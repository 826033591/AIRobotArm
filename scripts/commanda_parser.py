import mycobot_control

# 只适用于单行的命令行 pass
def pass_execute_command(instance,command_str):
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

def execute_command(instance, command_str):
    try:
        #将命令字符串分割成多行
        commands = command_str.strip().split('\n')
        for cmd in commands:
            # 移除空白字符，并分割对象名和方法
            cmd = cmd.strip()
            if not cmd:
                continue

            # 移除 robot.
            if cmd.startswith("robot."):
                cmd = cmd[6:]

            # 分割方法名，和参数
            if '(' in cmd and cmd.endswith(")"):
                method_name, args_str = cmd.split('(', 1)
                method_name = method_name.strip() #删除前后空格
                args_str = args_str.rstrip(")") #删除右侧的）
                # 移除可能的空白字符，并按逗号分隔参数
                args = [arg.strip() for arg in args_str.split(',')] if args_str else []
            else:
                print(f"Invalid command format : {cmd}")
                continue

            if hasattr(instance, method_name):
                command_function = getattr(instance, method_name)
                if args:
                    # 将字符串参数转换为相应的类型，这里简单地使用eval
                    # 注意：eval() 可以执行任意代码，应该仅在信任输入时使用
                    processed_args = [eval(arg) for arg in args if arg]
                    command_function(*processed_args)
                else:
                    command_function()
            else:
                print(f"command {method_name}, not found in robot")
    except Exception as e:
        print(f"an error occurred while executing commands: {e}")


if __name__ == "__main__":

    robot = mycobot_control.MyCobotController("com4", 115200)
    gpt_command = "robot.move_to_zero()\n  robot.grab_position()\n   robot.plus_z_coords(20)"

    print(gpt_command)
    execute_command(robot, gpt_command)

