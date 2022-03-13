# Author: Ankur Patel
# 
# Python program to tag parts of speech after 
#   constructing a "most likely tag" model based 
#   on supplied training data. 
# Inputs a POS-tagged file, recording the most likely 
#  tags for each word. Output -> use model to POS tag a test file
# 

import re
# Extract POS tags into a dictionary
# IN: corpus; a contiguous string of POS-tagged text
# OUT: stochastic_model; a dictionary containing each word and its most 
#       often occuring part of speech
def train_model(corpus):
    stochastic_model = dict()
    # Word / Part of speech
    tagger_pair_pattern = r"([\w]+)/([\w]+)"
    # Split corpus along backslashes



def apply_tags():
    pass

if __name__ == '__main__':
    import sys
    training_file = ""
    test_file = ""
    file_with_tags = ""
