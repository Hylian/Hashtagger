from math import log
from random import choice
from string import ascii_lowercase

wordfile = open ('../data/shakespeare.txt', 'r')
words = ["START"]

def clean (word):
    ret = ""
    for c in word:
	if c in ascii_lowercase:
	    ret = ret + c
    return ret

for line in wordfile:
    cur_words = line.split ()
    if len (cur_words) == 0:
	words.append ("END")
	words.append ("START")
    for word in cur_words:
	word_clean = clean (word.lower ())
	if len (word_clean) > 0:
	    words.append (word_clean)

words.append ("END")

print words

count = dict ()

for i in range (len (words) - 1):
    if words [i] in count:
	count [words [i]].append (words [i + 1])
    else:
	count [words [i]] = [words[i + 1]]


while (True):
    cur_word = raw_input ("Please enter a starting word: ")

    while (cur_word != "END"):
	print cur_word,
	next_word = choice (count [cur_word])
	cur_word = next_word
