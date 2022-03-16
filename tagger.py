# Author: Ankur Patel
#
# Python program to tag parts of speech after
#   constructing a "most likely tag" model based
#   on supplied training data.
# 
# 

# Extract POS tags into a dictionary
# IN: corpus; a contiguous string of POS-tagged text
# OUT: stochastic_model; a dictionary containing each word and its most
#       often occuring part of speech

import re
import sys

def train_model(corpus: str):
    tag_list = []
    tag_set = dict(tag_list)
    stochastic_model = dict()
    # Word / Part of speech
    tagger_pair_pattern = r"([\S]+)/([\S]+)"
    # Split corpus along backslashes
    pair_matches = re.findall(tagger_pair_pattern, corpus)    

    # Create list of all tags associated with each word
    for current_word, current_tag in pair_matches:
        if current_word in tag_set:
            tag_set[current_word].append(current_tag)
        else:
            tag_set[current_word] = [current_tag]
    # For each word, select the most common tag and insert into model
    for word in tag_set:
        if word in stochastic_model:
            continue
        else:
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
    # Parse text into list of words
    # Remove brackets
    corpus = re.sub(r"[\[\]]", " ", raw_text)
    # delineate on whitespace
    corpus = re.findall(r"([\S]+)", corpus)
    for word in corpus:
        if word in s_model:
            current_tag = s_model[word]
            sys.stdout.write(word + "/" + current_tag + "\n")
        else:
            sys.stdout.write(word + "/NN" + "\n")
            

if __name__ == '__main__':
    
    # File I/O
    training_file_name = str(sys.argv[1])
    test_file_name = str(sys.argv[2])
    
    training_corpus = ""
    with open(training_file_name) as file:
        training_corpus = file.read()
        
    test_corpus = ""
    with open(test_file_name) as file:
        test_corpus = file.read()
        
    # Create part of speech model
    tagger_model = train_model(training_corpus)
    # Execute analysis on supplied text
    apply_tags(test_corpus, tagger_model)
    