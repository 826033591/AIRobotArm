import speech_to_text
import gpt_interaction
from mycobot_control import MyCobotController
import commanda_parser

def main():
    print("system is running! Please say your  command")

    while True:
        print("\n 请说出指令（说“退出”或者“OUT” 退出系统）")
        speech_input = speech_to_text.speech_to_text()

        if speech_input.lower() in ['退出',"out"]:
            print("system is closing!")
            break

        print(f"你说出的指令是：{speech_input}")

        # 生成代码指令
        generate_code = gpt_interaction.generate_control_code(speech_input)

        commanda_parser.execute_command(robot,generate_code)









if __name__ == "__main__":
    robot = MyCobotController('com4', 115200)
    main()