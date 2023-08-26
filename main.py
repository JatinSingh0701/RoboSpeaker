import pyttsx3


def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print("Welcome to RoboSpeaker")

    while True:
        what_to_speak = input("What you want to speak (type 'exit' to quit): ")

        if what_to_speak.lower() == 'exit':
            print("Exiting RoboSpeaker")
            break

        speak_text(what_to_speak)
