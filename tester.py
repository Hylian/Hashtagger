import sys, math
sys.path.insert(0, 'sentGen')
"""
from generator import get_all_data, load_data, generate, generate_multiple

get_all_data ()
for a in generate_multiple ("#yolo", 10):
    print a
    """

sys.path.insert(0, 'Predictor')
from predictor2 import train, set_priors, predictor_func, run_tests
from predictor_helper import test

"""
#run_tests (predictor_func)

while (True):
    text = raw_input ("Enter a tweet: ")
    ex = text.split ()

    res = test (ex, predictor_func)
    best = res [0]
    worst = res [1]

    print ' '.join (ex)
    print "MOST RELEVANT HASHTAGS"
    for x in best:
	print x [0], x [1]
    print "\nLEAST RELEVANT HASHTAGS"
    for x in reversed (worst):
	print x [0], x [1]
	"""
