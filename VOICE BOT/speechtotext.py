import speech_recognition as sr
from texttospeech import texttospeechf


def speechtotextf():
    while(1):
        r = sr.Recognizer()
        texttospeechf("I am listening go Ahead"),print("say something")
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                audiototext= r.recognize_google(audio)
                print("recognised")
                audiototext=audiototext.lower()
                print(audiototext)
            except sr.RequestError as e: 
                print("Could not request results; {0}".format(e)) 
            except sr.UnknownValueError: 
                print("unknown error occured") 
        return audiototext


    