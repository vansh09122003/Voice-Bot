import pyttsx3 as pt

def texttospeechf(Mytext):
	engine = pt.init()
	engine.setProperty('rate', 150) 
	engine.say(Mytext) 
	engine.runAndWait() 

