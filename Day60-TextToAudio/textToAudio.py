#This will read the text and then save it to an audio file in the format mentioned like mp3/wav etc
from gtts import gTTS
import os
f = open('f.txt')
x= f.read().lower()
language = 'en'
audio = gTTS(text=x,lang=language,slow=False)

audio.save('of.mp3')