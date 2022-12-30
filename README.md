# nlp-project

Simple program to compare similarity between two documents.

For each documents we normalize text, remove stop words and steem words. Later we create word frequencies and compare the similarity between distributions.

Methods used:
 - Jaccard index: This method compares the similarity between two word frequency distributions by calculating the ratio of the size of the intersection of the two sets to the size of the union of the two sets. The Jaccard index is calculated by first creating sets for each distribution by extracting the unique words from the distributions. Then, the Jaccard index is calculated using the following formula: Jaccard index = |A intersection B| / |A union B| where A and B are the sets representing the two word frequency distributions. The Jaccard index will range from 0 to 1, with a value of 1 indicating that the two sets are identical and a value of 0 indicating that the two sets have no elements in common.

 - Cosine similarity: This method compares the similarity between two word frequency distributions by calculating the angle between two vectors, where each vector represents a word frequency distribution. The vectors are created by assigning a weight to each unique word in the distribution based on its frequency. The cosine similarity is calculated by taking the dot product of the two vectors and dividing it by the product of their magnitudes. The cosine similarity will range from -1 to 1, with a value of 1 indicating that the two vectors are identical and a value of -1 indicating that the two vectors are completely dissimilar.

 - Euclidean distance: This method calculates the distance between two vectors, where each vector represents a word frequency distribution. To calculate the Euclidean distance, you can subtract the frequency of each word in one distribution from the frequency of the same word in the other distribution, square the differences, and sum them up. Then, you can take the square root of the sum to get the Euclidean distance between the two vectors.

 - KL divergence: This method measures the difference between two word frequency distributions by calculating the difference between the entropies of the two distributions.