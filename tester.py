import sys
sys.path.insert(0, 'Predictor')

from predictor import train, set_priors, predictor_func run_tests

print "Begin Training"
train ()
print "Training Complete"
print "Setting Priors"
set_priors ()
print "Priors Set"
run_tests (predictor_func)

#from generator import get_all_data, load_data, generate, generate_multiple

#get_all_data ()
#for a in generate_multiple ("#yolo", 10):
#    print a
