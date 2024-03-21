import speech_to_text
import command_parser
import mycobot_control

def main():
    print("system is running! Please say your  command")

    while True:
        print("\n 请说出指令（说“退出”或者“OUT” 退出系统）")
        speech_input = speech_to_text.speech_to_text()

        if speech_input.lower() in ['退出',"out"]:
            print("system is closing!")
            break

        print(f"你说出的指令是：{speech_input}")

        #指令传输到chatgpt来省城控制指令。
        control_command = command_parser.parse_and_execute_command(speech_input)




if __name__ == "__main__":
    None
