import pyttsx3

engine = pyttsx3.init()
engine.say("she updated her status on whatsApp")
engine.runAndWait()

import pyjokes

# print("i am printing pyjokes")

joke = pyjokes.get_joke()
print(joke)

import os

# Specify the directory path
directory_path = input("Enter the directory path: ")

# Check if the directory exists and if the path is accessible
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # Get the list of all files and directories
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    
    for item in contents:
        print(item)
else:
    print(f"The directory '{directory_path}' does not exist or cannot be accessed.")

