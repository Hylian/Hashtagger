import sys
sys.path.insert(0, 'sentGen')

from generator import get_all_data, load_data, generate, generate_multiple

get_all_data ()
for a in generate_multiple ("#yolo", 10):
    print a
