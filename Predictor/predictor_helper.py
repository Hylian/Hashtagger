import numpy

freq = dict ()
words = []
examples = []
num_train = 1000
num_test = 1000

#utilities
def checkChar (c):
    return 0 <= ord (c) and ord(c) < 128

def clean (word):
    ret = filter (checkChar, word)
    ret = ret.encode ("ascii", "ignore")
    return ret

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

    words += read_in ('../csvconvert/yolotweets.csv.pickle')
    #words += read_in ('../csvconvert/iphonetweets.csv.pickle')
    #words += read_in ('../csvconvert/educationtweets.csv.pickle')
    #words += read_in ('../csvconvert/newstweets.csv.pickle')
    words += read_in ('../csvconvert/syriatweets.csv.pickle')
    #words += read_in ('../csvconvert/economytweets.csv.pickle')

def get_exmample (

get_all_data ()
