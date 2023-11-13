import words
import random
import os

word_list = words.generate_random_words(5)
length_words = len(word_list)
count = 0  # Initialize count outside the function
centered_arrow = "=>".center(-40)

def check_user_input():
    global count, score  # Declare count and score as global variables
    if count <= length_words - 1:
        random_word = word_list[count]
        print("**************************************")
        if os.name == 'nt':
            os.system('cls')
        print("******************************************")
        print(f"{random_word.center(40)}")
        print("******************************************")
        user_input = input(centered_arrow)
        print("**************************************")
        for word in word_list:
            if user_input.lower() == word.lower():
                count += 1
                return True
        print("Incorrect! Try again.")
        return True
    else:
        print("Thank you for typing!!!")
        return False

while check_user_input():
    continue
