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
import re 
from sklearn import metrics
import sys

# Helper function to extract list of tags from tagged text
# IN: 
#   file_contents: raw string
# OUT: 
#   tag_list: list containing tags
def extract_tags(file_contents):
    tagger_pair_pattern = r"[\S]+/([\S]+)"
    file_contents = re.sub(r"[\[\]]", " ", file_contents)
    return re.findall(tagger_pair_pattern, file_contents)
    

def score_pos_tags(actual: list, predicted: list):
    # Cast each list as a pandas series for analysis
    actual_series = pd.Series(actual, name='Actual')
    predicted_series = pd.Series(predicted, name='Predicted')
    # zip together both lists into a 2d array
    sys.stdout.write("Accuracy score: " + str(metrics.accuracy_score(actual_series, predicted_series)) + "\n")
    sys.stdout.write(str(pd.crosstab(actual_series, predicted_series)))
    

if __name__ == '__main__':
    
    tagged_file_name = str(sys.argv[1])
    test_key_file_name = str(sys.argv[2])
    
    tagged_corpus = ""
    test_key_corpus = ""
    
    tagged_data = []
    test_data = []
    
    with open(tagged_file_name) as file:
        tagged_corpus = file.read()
        
        
    with open(test_key_file_name) as file:
        test_key_corpus = file.read()
    
    tagged_data = extract_tags(tagged_corpus)
    test_data = extract_tags(test_key_corpus)
    
    score_pos_tags(actual=test_data, predicted=tagged_data)