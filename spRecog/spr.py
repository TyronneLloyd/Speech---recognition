import datetime
import  speech_recognitionp

recognizer = speech_recognition.Recognizer()
now = datetime.datetime.now()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

            f = open("out.txt", "a")
            f.write(text + "\n")

            if text == "stop":
                exit()
                

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
