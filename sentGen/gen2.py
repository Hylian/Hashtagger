from math import log
from random import choice
from string import ascii_lowercase
import numpy
import pickle

NUM_FILES = 50

wordfile = open ('../data/shakespeare.txt', 'r')
words = []

def clean (word):
    ret = ""
    for c in word:
	if c in ascii_lowercase:
	    ret = ret + c
    return ret

def is_url (word):
    if word [0:4] == "http":
	return True
    return False

def read_shakespeare ():
    words = ["START"]
    for line in wordfile:
	cur_words = line.split ()
	#if len (cur_words) == 0:

	for word in cur_words:
	    if (word [len (word) - 1] == '.'):
		words.append ("END")
		words.append ("START")

	    word_clean = clean (word.lower ())
	    if len (word_clean) > 0:
		words.append (word_clean)
    words.append ("END")

count = dict ()
hdict = dict ()

def process (words):
    for i in range (len (words) - 1):
	if words [i] not in count:
	    count [words [i]] = dict ()

	if words [i + 1] in count[words [i]]:
	    count [words[i]][words[i + 1]] += 1.0
	else:
	    count [words[i]][words[i + 1]] = 1.0


for i in range (NUM_FILES):
    data = pickle.load (open ('../scraper/tweets' + str (i), 'rb'))
    
    for pair in data:
	text = pair [0]
	hashtags = pair [1]
	words.append ("START")

	for hashtag in hashtags:
	    if hashtag not in hdict:
		hdict [hashtag] = dict ()
	    for word in text:
		if is_url (word):
		    continue
	    
		words.append (word)
		
		print hashtag, word
		if word in hdict [hashtag]:
		    hdict[hashtag][word] += 1.0
		else:
		    hdict[hashtag][word] = 1.0 
	
	words.append ("END")

process (words)
print "Dictionary has been processed for shakespeare"


def print_dict (d):
    for word in d:
	print d[word], word
    print "\n"

#merge dictionaries
def merge (cur_word, hashtag):
    if cur_word not in count:
	return hdict [hashtag]
    elif cur_word not in hdict:
	return count [cur_word]

    a = count [cur_word]
    b = hdict [hashtag]

    ret = dict ()
    for word in a:
	ret [word] = a [word]
	if word in b:
	    ret [word] *= b [word]
	else:
	    ret [word] *= .1
    for word in b:
	if word in ret:
	    continue
	ret [word] = b [word]

    return ret

def normalize (d):
    weight_sum = 0.0
    for next_word in d:
	weight_sum += d[next_word] 

    for next_word in d:
	d [next_word] /= weight_sum
	#print d[next_word],
    #print "\n\n"
    

    return d

def get_sentence (word, hashtag):
    cur_word = word
    ret = ""

    while (cur_word != "END"):
	ret = ret + " " + cur_word
	prob = normalize (merge (cur_word, hashtag))
	#prob = normalize (count [cur_word])
	p = numpy.random.uniform ()
	print_dict (prob)

	next_word = ""
	for word in prob:
	    p -= prob [word]
	    if p <= 1e-9:
		next_word = word
		break

	cur_word = next_word

    return ret 

while (True):
    cur_word = raw_input ("Choose a Starting Word: ")
    cur_word = cur_word.lower ()
    cur_hash = raw_input ("Choose a Hashtag: ")

    if (cur_word not in count):
	print "Not a valid word"
	continue

    if (cur_hash not in hdict):
	print "Not a valid hashtag"
	continue

    print_dict (hdict [cur_hash])
    sent = get_sentence (cur_word, cur_hash)
    print sent
