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
import pandas as pd 
from sklearn import metrics
import sys

def parse_text(corpus):
    pass

def score_pos_tags(predicted: list, actual: list):
    # Cast each list as a pandas series for analysis
    predicted_series = pd.Series(predicted, name='Predicted')
    actual_series = pd.Series(actual, name="Actual")
    # zip together both lists into a 2d array
    confusion_mat = metrics.confusion_matrix(actual_series, predicted_series)
    sys.stdout.write(pd.crosstab(actual_series, predicted_series))
    sys.stdout.write("Accuracy score: " + metrics.accuracy_score(actual_series, predicted_series))

if __name__ == '__main__':
    
    tagged_file_name = str(sys.argv[1])
    test_key_file_name = str(sys.argv[2])
    
    tagged_corpus = ""
    test_key_corpus = ""
    
    with open(tagged_file_name) as file:
        tagged_corpus = file.read()
        
        
    with open(test_key_file_name) as file:
        test_key_corpus = file.read()
    