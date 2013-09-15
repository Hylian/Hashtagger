import numpy, pickle
from predictor import predictor_func

NUM_FILES = 100
freq = dict ()
words = []
examples = []

cur_example = 0
num_train = 1000
num_test = 1000
score = 0.0

#utilities
def checkChar (c):
    return 0 <= ord (c) and ord(c) < 128

def clean (word):
    ret = filter (checkChar, word)
    ret = ret.encode ("ascii", "ignore")
    return ret

def is_url (word):
    if word [0:4] == "http":
	return True
    return False
#input

def read_in (file_addr):
    data = pickle.load (open (file_addr, 'rb'))
    words = []
    global hdict

    for pair in data:
	text = pair [0]
	hashtags = pair [1]

	clean_text = []
	clean_hashtags = []

	for hashtag in hashtags:
	    clean_hashtags.append (clean (hashtag))
	    for word in text:
		if is_url (word):
		    continue
	    
		clean_text.append (clean (word))
	examples.append ([clean_text, clean_hashtags])

def get_all_data ():
    for i in range (NUM_FILES):
	read_in ('../scraper/tweets' + str (i))

    read_in ('../csvconvert/yolotweets.csv.pickle')
    #read_in ('../csvconvert/iphonetweets.csv.pickle')
    #read_in ('../csvconvert/educationtweets.csv.pickle')
    #read_in ('../csvconvert/newstweets.csv.pickle')
    read_in ('../csvconvert/syriatweets.csv.pickle')
    #read_in ('../csvconvert/economytweets.csv.pickle')

def get_example ():
    if (cur_example >= num_train):
	return False

    ex = examples [cur_example]
    cur_example += 1
    return ex

def run_tests ():
    ex = examples [cur_example]
    distrib = predictor_func (ex [0])
    cur_score = 0
    for hashtag in distrib:
	if hashtag not in ex [1]:
	    cur_score += log (1 - distrib [hashtag])
    for hashtag in ex [1]:
	if hashtag in distrib:
	    cur_score += log (distrib [hashtag])
	else:
	    cur_score += -1000

    score += cur_score
    cur_example += 1

get_all_data ()
