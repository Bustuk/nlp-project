# nlp-project

Simple program to compare similarity between two documents.

Methods used:
 - Jaccard index: This method compares the similarity between two word frequency distributions by calculating the ratio of the size of the intersection of the two sets to the size of the union of the two sets. The Jaccard index is calculated by first creating sets for each distribution by extracting the unique words from the distributions. Then, the Jaccard index is calculated using the following formula: Jaccard index = |A intersection B| / |A union B| where A and B are the sets representing the two word frequency distributions. The Jaccard index will range from 0 to 1, with a value of 1 indicating that the two sets are identical and a value of 0 indicating that the two sets have no elements in common.

 - Cosine similarity: This method compares the similarity between two word frequency distributions by calculating the angle between two vectors, where each vector represents a word frequency distribution. The vectors are created by assigning a weight to each unique word in the distribution based on its frequency. The cosine similarity is calculated by taking the dot product of the two vectors and dividing it by the product of their magnitudes. The cosine similarity will range from -1 to 1, with a value of 1 indicating that the two vectors are identical and a value of -1 indicating that the two vectors are completely dissimilar.

 - Euclidean distance: This method calculates the distance between two vectors, where each vector represents a word frequency distribution. To calculate the Euclidean distance, you can subtract the frequency of each word in one distribution from the frequency of the same word in the other distribution, square the differences, and sum them up. Then, you can take the square root of the sum to get the Euclidean distance between the two vectors.

 - KL divergence: This method measures the difference between two word frequency distributions by calculating the difference between the entropies of the two distributions.

 - Word Mover's Distance (WMD) is a measure of the distance between two documents represented as sequences of words. It was introduced by Matt Kusner et al. in the paper "From Word Embeddings To Document Distances" (https://proceedings.mlr.press/v37/kusnerb15.pdf).
 WMD is based on the idea of "earth mover's distance", which is a measure of the distance between two probability distributions. In the context of WMD, the probability distributions are represented by the words in the two documents, and the distance between the distributions is the minimum amount of "work" that would be required to transform one distribution into the other. This "work" is defined as the sum of the distances that each word in the first document would need to "travel" in order to become the corresponding word in the second document.
 For this method we will be using Word2vec Model pretrained by Google - it requires downloading over 1,5GB model so this methods should require additional acceptance


Example code can be found in example.py. Output for example code:

```
(myenv) (base) python examply.py
Do you want to use WMD method? It requires downloading a google model (over 1,5GB). (y/n)
y
Same text
-----------------------
Jaccard index: (1 - best, 0 - worst)  1.0
Cosine similarity: (1 - best, 0 - worst)  1.0
KL divergence: (0 - best, ∞ - worst )  0.0
Euclidean distance: (0 - best, ∞ - worst ) 0.0
Word mover's distance: (0 - best, ∞ - worst ) 0.0
-----------------------
Different text
-----------------------
Jaccard index: (1 - best, 0 - worst)  0.0
Cosine similarity: (1 - best, 0 - worst)  0.0
KL divergence: (0 - best, ∞ - worst )  5
Euclidean distance: (0 - best, ∞ - worst ) 3.872983346207417
Word mover's distance: (0 - best, ∞ - worst ) 1.2560052766041012
-----------------------
Similar text
-----------------------
Jaccard index: (1 - best, 0 - worst)  0.07692307692307693
Cosine similarity: (1 - best, 0 - worst)  0.20412414523193154
KL divergence: (0 - best, ∞ - worst )  5.386294361119891
Euclidean distance: (0 - best, ∞ - worst ) 4.0
Word mover's distance: (0 - best, ∞ - worst ) 0.9114290809729197
-----------------------
```