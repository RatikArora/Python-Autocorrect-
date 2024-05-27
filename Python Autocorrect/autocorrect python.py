import pandas as pd
import textdistance
import re
from collections import Counter
words = []
with open('making  actual things/Python Autocorrect/datasets/book.txt', 'r',encoding="UTF-8") as f:
    file_name_data = f.read()
    file_name_data=file_name_data.lower()
    words = re.findall('\w+',file_name_data)
V = set(words)
print(f"The first ten words in the text are: \n{words[0:10]}")
print(f"There are {len(V)} unique words in the vocabulary.")


word_freq_dict = {}  
word_freq_dict = Counter(words)
print(word_freq_dict.most_common()[0:10])


probs = {}     
Total = sum(word_freq_dict.values())    
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k]/Total


def my_autocorrect(input_word):
    input_word = input_word.lower()
    # if input_word in V:
    #     return('Your word seems to be correct')
    # else:
    candidates = [word for word in V if abs(len(word) - len(input_word)) <= 2]
    similarities = [1 - textdistance.Jaccard(qval=2).distance(word, input_word) for word in candidates]
    
    df = pd.DataFrame({
        'Word': candidates,
        'Similarity': similarities,
        'Prob': [probs[word] for word in candidates]
    })
    
    output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
    return output

print(my_autocorrect("howeve"))
