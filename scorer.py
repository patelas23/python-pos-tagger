# Author: Ankur Patel

# Helper file to generate confusion statistics for 
#   tagger.py by grading its output against a gold standard file
# IN: 
#   tag_out: tagger.py output, dictionary{word: tag}
#   g_std: hand-tagged gold standard, dictionary{word:tag}
# OUT:
#   confusion_mat: 2d matrix containing
#       rows (actual): sequence of tags from gold standard
#       cols(predicted): sequence of tagger.py tags
# 
import sys


def score_pos_tags(tag_out, g_std):
    # Extract word/tag pairs from each corpus
    
    # Compare each sequence of tags to find deviation from standard
    # Store each new word and it's pos
    # Store each guessed word and it's pos
    # zip together both lists into a 2d array
    pass

if __name__ == '__main__':
    
    tagged_file_name = str(sys.argv[1])
    test_key_file_name = str(sys.argv[2])
    
    tagged_corpus = ""
    test_key_corpus = ""
    
    with open(tagged_file_name) as file:
        tagged_corpus = file.read()
        
        
    with open(test_key_file_name) as file:
        test_key_corpus = file.read()
    