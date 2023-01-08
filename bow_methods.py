import math
from utils import get_word_freq

def jaccard_index(dist1, dist2):
  # Extract the unique words from each distribution
  set1 = set(dist1.keys())
  set2 = set(dist2.keys())
  
  # Calculate the intersection of the two sets
  intersection = set1.intersection(set2)
  
  # Calculate the union of the two sets
  union = set1.union(set2)
  
  # Calculate the Jaccard index
  jaccard_index = len(intersection) / len(union)
  
  return jaccard_index

def kl_divergence(dict1, dict2):
  # Initialize the KL divergence to 0
  kl_div = 0

  # Loop through all the words in dict1
  for word, count1 in dict1.items():
    # If the word is not in dict2, add the count from dict1 to the KL divergence
    if word not in dict2:
      kl_div += count1
    else:
      # If the word is in dict2, add the count from dict1 times the log of the ratio of the counts to the KL divergence
      count2 = dict2[word]
      kl_div += count1 * math.log(count1 / count2)

  # Return the KL divergence
  return kl_div

def cosine_similarity(dic1,dic2):
    numerator = 0
    dena = 0
    for key1,val1 in dic1.items():
        numerator += val1*dic2.get(key1,0.0)
        dena += val1*val1
    denb = 0
    for val2 in dic2.values():
        denb += val2*val2
    return numerator/math.sqrt(dena*denb)

def euclidean_distance(dict1, dict2):
  # Initialize the sum of squared differences to 0
  sum_squared_differences = 0

  # Loop through all the words in dict1
  for word, count1 in dict1.items():
    # If the word is in dict2, add the squared difference between the counts to the sum
    if word in dict2:
      count2 = dict2[word]
      sum_squared_differences += (count1 - count2) ** 2
    else:
      # If the word is not in dict2, add the square of the count from dict1 to the sum
      sum_squared_differences += count1 ** 2

  # Loop through all the words in dict2 that are not in dict1
  for word, count2 in dict2.items():
    if word not in dict1:
      # Add the square of the count from dict2 to the sum
      sum_squared_differences += count2 ** 2

  # Return the square root of the sum of squared differences
  return math.sqrt(sum_squared_differences)

def print_all(dict1, dict2):
  print("Jaccard index: (1 - best, 0 - worst) ", jaccard_index(dict1, dict2))
  print("Cosine similarity: (1 - best, 0 - worst) ", cosine_similarity(dict1, dict2))
  print("KL divergence: (0 - best, ∞ - worst ) ", kl_divergence(dict1, dict2))
  print("Euclidean distance: (0 - best, ∞ - worst )", euclidean_distance(dict1, dict2))

def get_similarity(text1, text2):
    dict1 = get_word_freq(text1)
    dict2 = get_word_freq(text2)
    return print_all(dict1, dict2)