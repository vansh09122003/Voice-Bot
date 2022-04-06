from texttospeech import texttospeechf
from speechtotext import speechtotextf
from wakeup import wakeupf
from movie_detail import movie_review 
from movie_detail import actors
import subprocess


while(1):
    wake=wakeupf()
    if wake==True:
        print("wake")
        gettext=speechtotextf()
        print(gettext)
        gettext=gettext.lower()
        if "hello" in gettext or "hey" in gettext:
            texttospeechf("Tell me what to do I am there for U")
            gettext=speechtotextf()
        elif "chrome" in gettext  or "Chrome" in gettext:
            texttospeechf("Opening Chrome")
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            ##os.startfile(r"C:\Users\Vansh Tanwani\Desktop\Google Chrome.lnk") 
        elif "movie review" in gettext or "review" in gettext or 'movie' in gettext:
            for word in ["movie","review"]:
                if word in gettext:
                    gettext=gettext.replace(word,"")
            movie_review(gettext)
            texttospeechf("do you want to know more actors")
            affermation=speechtotextf()
            if affermation=="yes" or affermation=="Yes":
                actors(gettext)      
    else:
        wake=wakeupf()
        