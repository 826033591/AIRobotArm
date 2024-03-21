import speech_recognition as sr


def speech_to_text():
    # 初始化识别器
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("请说话...")
        audio = recognizer.listen(source)

        try:
            # 使用Google的语音识别服务
            text = recognizer.recognize_google(audio, language='zh-CN')
            # text = recognizer.recognize_google(audio, language='en-US')
            print("you said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


# 测试函数
if __name__ == "__main__":
    speech_to_text()
