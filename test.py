
# -*- coding: utf-8 -*-
#import sys
#from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')
from flask import request
from flask import Flask, url_for
import numpy as np
import pandas as pd
from collections import Counter
import deepcut
import speech_recognition as sr

## Encoding function

# In[10]:
import pickle
def save_obj(obj, name ):
	with open('obj/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

app = Flask(__name__)

@app.route('/api/listen')
def listen():
	cnt = Counter()
	karaoke_dict = load_obj("karaoke_dict_new")

	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    # print("ร้องเพลงสิิ!")
	    audio = r.listen(source, phrase_time_limit=15)
	 
	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    text = r.recognize_google(audio, language='th-TH')
	    # print("You said: " + text)
	    # print("Guessing the song....")
	    tokens = deepcut.tokenize(text)
	    for j in range(len(tokens)-6):
	    	words = "".join(tokens[j:j+6])
	    	if words in karaoke_dict:
	    		cnt[karaoke_dict[words]] += 1
	    return text+str(cnt)
	except sr.UnknownValueError:
	    return "คุณเป็นนักร้องเสียงเพี้ยนนนนนนนน"
	except sr.RequestError as e:
	    return "พังจ้าาา; {0}".format(e)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555, debug=True)

