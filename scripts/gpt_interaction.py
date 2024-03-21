import openai


def generate_control_code(prompt):
    """
  使用ChatGPT根据提供的提示（prompt）生成控制机械臂的代码。
  """
    openai.api_key = 'your_openai_api_key_here'

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        code = response.choices[0].text.strip()
        return code
    except Exception as e:
        print(f"发生错误: {e}")
        return ""



def main():
    print("欢迎使用语音控制的myCobot机械臂")
    print("请说出控制机械臂的指令，比如'向前移动10厘米'")

    while True:
        user_input = input("请输入指令（或输入'exit'退出）: ")
        if user_input.lower() in ['exit', 'quit']:
            print("退出程序")
            break

        # 假设speech_to_text模块的输出已经保存在user_input变量中
        # 这里我们将其直接作为prompt发送给ChatGPT
        prompt = f"根据以下指令生成控制myCobot机械臂的Python代码：\n\n'{user_input}'\n\n代码："
        generated_code = generate_control_code(prompt)

        if generated_code:
            print("生成的控制代码：")
            print(generated_code)
        else:
            print("无法生成控制代码，请尝试不同的指令。")


if __name__ == "__main__":
    main()
