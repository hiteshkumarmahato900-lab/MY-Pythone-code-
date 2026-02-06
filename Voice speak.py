# first go to terminal and write pip install pyttsx3 
#after install paste this code and run  
import pyttsx3
engine = pyttsx3.init()

# write here what's you want to speak 

engine.say('how are you') 
engine.runAndWait()
