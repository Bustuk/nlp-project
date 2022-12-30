from freq import get_word_freq
from methods import print_all
import math
def get_similarity(text1, text2):
    dict1 = get_word_freq(text1)
    dict2 = get_word_freq(text2)
    return print_all(dict1, dict2)

text1 = "This is a sample text. We will see how similar it is to other texts"
text2 = "Completely diffferent no words in common. It has nothing in common with the other"
text3 = "This is another text. It's somehow similar to the first text but also have something in common with the other"

print('Same text')
print('-----------------------')
get_similarity(text1, text1)
print('-----------------------')

print('Different text')
print('-----------------------')
get_similarity(text1, text2)
print('-----------------------')

print('Similar text')
print('-----------------------')
get_similarity(text2, text3)
print('-----------------------')