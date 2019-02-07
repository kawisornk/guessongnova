
import numpy as np
import pandas as pd
from collections import Counter
import deepcut
# ## Encoding function

# In[10]:

import pickle
def save_obj(obj, name ):
	with open('obj/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)



import speech_recognition as sr

if __name__ == '__main__':
	cnt = Counter()
	karaoke_dict = load_obj("karaoke_dict")

	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("ร้องเพลงสิ!")
	    audio = r.listen(source)
	 
	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    text = r.recognize_google(audio, language='th-TH')
	    print("You said: " + text)
	    print("Guessing the song....")
	    tokens = deepcut.tokenize(text)
	    for j in range(len(tokens)-6):
	    	words = "".join(tokens[j:j+6])
	    	if words in karaoke_dict:
	    		cnt[karaoke_dict[words]] += 1
	    print(cnt)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))