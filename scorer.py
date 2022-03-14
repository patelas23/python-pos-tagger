# Author: Ankur Patel

# Helper file to generate confusion statistics for 
#   tagger.py by grading its output against a gold standard file
# IN: 
#   tag_out: tagger.py output
#   g_std: hand-tagged gold standard
# OUT:
#   confusion_mat: 2d matrix containing
#       rows: sequence of tags from gold standard
#       cols: sequence of tagger.py tags
# 
def score_pos_tags(tag_out, g_std):
    # Extract word/tag pairs from each corpus
    # Store each new word and it's pos
    # Store each guessed word and it's pos
    # zip together both lists into a 2d array
    pass