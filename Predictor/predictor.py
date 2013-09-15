import numpy
from predicotr_helper import run_tests 

freq = dict ()
hfreq = dict ()

def train ():
    while (ex = get_example ()):
	text = ex [0]
	hashtags = ex [1]
	for word in text:
	    for hashtag in hashtags:
		if hashtag not in hfreq:
		    hfreq [hashtag] = dict ()
		
		if text not in hfreq [hashtag]:
		    hfreq [hashtag][text] = 0
		
		hfreq [hashtag][text] += 1

	    if word not in freq:
		freq [word] = 0
	    freq [word] += 1

def predictor_func ():
    ret = dict ()
    
    
train ()
run_tests ()
