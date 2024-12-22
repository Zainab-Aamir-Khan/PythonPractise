import pyttsx3
engine = pyttsx3.init()
engine.say("i am good at coding")
engine.runAndWait()

import pyjokes

# print("i am printing pyjokes")

joke = pyjokes.get_joke()
print(joke)