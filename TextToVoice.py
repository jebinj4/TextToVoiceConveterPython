from gtts import gTTS
import os
mytext=input('Enter your Text:')
language='en'

myobj=gTTS(text=mytext,
           lang=language,slow=False)

myobj.save('welcome2.mp3')
os.system('welcome2.mp3')