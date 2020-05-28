import speech_recognition as sr
import os
from gtts import gTTS

lan="en"
r=sr.Recognizer()
mic=sr.Microphone()
with mic as sour:
	say="Speak anything:- "
	play=gTTS(text=say,lang=lan,slow=False)
	play.save("p.mp3")
	os.system("mpg123 p.mp3")
	r.adjust_for_ambient_noise(sour)
	print("Speak anything:- ")
	audio=r.listen(sour,timeout=5, phrase_time_limit=5)
try:
	teext=r.recognize_google(audio)
	""",language='gu-IN'"""
	print("you said:-",teext)
	play=gTTS(text=teext,lang=lan,slow=False)
	play.save("p.mp3")
	os.system("mpg123 p.mp3")
	t=teext.lower()
	os.system(t)
	print(t)
	with open("logs.txt","a") as f:
		f.write(f"{teext}\r\n")
	'''if(teext=='Aircel'):
		print(teext)
		os.system(teext.lower())'''
except:
	print("error")

with mic as sour:
	play=gTTS(text="Exit or continue",lang=lan,slow=False)
	play.save("p.mp3")
	os.system("mpg123 p.mp3")
	r.adjust_for_ambient_noise(sour)
	print("Exit or continue:- ")
	audio=r.listen(sour,timeout=5, phrase_time_limit=5)
try:
	teext1=r.recognize_google(audio)
	if(teext1=='continue'):
		print(teext1)
		os.system("python spee.py")
	else:
		os.system("python spee.py")
	with open("logs.txt","a") as f:
		f.write(f"{teext1}\r\n")
except:
	print("error 2")