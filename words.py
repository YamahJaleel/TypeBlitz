import os
import random

# Generate random list of Words to be used from the Words.txt 
def generate_random_words(n):
    os.chdir(r'C:\Users\Jalee\Code\Python\GitHub\TypeBlitz')            # Change current OS directory to wherever the Words.txt file is located
    list_words = []                                                     # Initialize list of words 
    file = open('Words.txt')                                            # Open the Words.txt file for reading words
    list_words = [word.strip().lower() for word in file]                # Iterate through each word in the Words.txt file and store in list of words 
    random_index_1 = random.randint(1, 1499 - n)                        # Generate a random index 1 
    random_index_2 = random_index_1 + n                                 # Generate a random index 2 
    return list_words[random_index_1:random_index_2]                    # Return sublist of words where n is the length of the list and each index is in the range of 1 and 1500