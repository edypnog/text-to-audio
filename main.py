from gtts import gTTS
import os

# Enter the text in string format which you want to convert into audio
myText = "Hi this is my first bot"

# Specify the language
language = 'en'

# Create an instance of gTTS class
myobj = gTTS(text=myText, lang=language, slow=False)

# Method to create your audio file in mp3 format
myobj.save("helloworld.mp3")
print("Audio saved")

# This will play your audio file
os.system("helloworld.mp3")