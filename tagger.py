# Author: Ankur Patel
#
# Python program to tag parts of speech after
#   constructing a "most likely tag" model based
#   on supplied training data.
# Inputs a POS-tagged file, recording the most likely
#  tags for each word. 
# Output: use model to POS tag a test file
#

# Extract POS tags into a dictionary
# IN: corpus; a contiguous string of POS-tagged text
# OUT: stochastic_model; a dictionary containing each word and its most
#       often occuring part of speech

import re

def train_model(corpus):
    tag_list = []
    tag_set = dict(tag_list)
    stochastic_model = dict()
    # Word / Part of speech
    tagger_pair_pattern = r"([\w]+)/([\w]+|?)"
    # Split corpus along backslashes
    pair_matches = re.findall(tagger_pair_pattern, corpus)

    # Create list of all tags associated with each word
    for current_word, current_tag in pair_matches:
        if current_word in tag_set:
            tag_set[current_word].append(current_tag)
        else:
            tag_set[current_word] = []
    # For each word, select the most common tag and insert into model
    for word in tag_set:
        current_set = tag_set[word]
        chosen_tag = max(current_set, key=current_set.count)
        stochastic_model[word] = chosen_tag
        
    return stochastic_model

# Use generated stochastic model to apply part of speech tags
# to the given text file. Unidentifiable words are assumed
# to be nouns (NN).
# IN:
#   raw_text: sequence of words to be tagged
#   s_dict: stochastic model of most-likely tags
# OUT:
#   tagged_text: sequence of tuples containing each word and its tag
def apply_tags(raw_text: str, s_model: dict):
    
    for word in raw_text:
        if word in s_model:
            current_tag = s_model[word].value()
            pass


if __name__ == '__main__':
    import sys
    
    # File I/O
    # # Assuming each argument is separated by whitespace
    training_file_name = str(sys.argv[1])
    test_file_name = str(sys.argv[2])
    
    training_corpus = ""
    
    sys.stdout.write("hello there")
    
    # test_file_id = re.sub(pattern=r".txt", repl="", string=test_file_name)
    # tagged_file = test_file_id + "-tagged.txt"
    
    # with open(training_file_name) as file:
        # training_corpus = file.read()
        
    # Create part of speech model

    # Execute analysis on supplied text
    # training_data = train_model(training_corpus)
    
    
    
