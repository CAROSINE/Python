# Now installing the pyttsx3 library by using pip install command
# After installing, we can use it as a Speaker
import pyttsx3
engine = pyttsx3.init()
engine.say("By using the pyttsx3 library, we can convert text to speech")
engine.runAndWait()