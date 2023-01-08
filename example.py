from bow_methods import get_similarity
from wmd import WMD
text1 = "This is a sample text. We will see how similar it is to other texts"
text2 = "Completely diffferent no words in common. It has nothing in common with the other"
text3 = "This is another text. It's somehow similar to the first text but also have something in common with the other"

print('Do you want to use WMD method? It requires downloading a google model (over 1,5GB). (y/n)')
loadWMD = input()
useWMD = loadWMD == 'y'
if useWMD:
    wmd = WMD()

print('Same text')
print('-----------------------')
get_similarity(text1, text1)
if useWMD:
    wmd.get_similarity(text1, text1)
print('-----------------------')

print('Different text')
print('-----------------------')
get_similarity(text1, text2)
if useWMD:
    wmd.get_similarity(text1, text2)
print('-----------------------')

print('Similar text')
print('-----------------------')
get_similarity(text2, text3)
if useWMD:
    wmd.get_similarity(text2, text3)
print('-----------------------')