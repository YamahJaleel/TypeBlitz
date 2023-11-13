import words
import random

word_list = words.generate_random_words(5)

def check_user_input():
    #print([word.split() for word in word_list])
    random_word = word_list[random.randint(0,len(word_list) - 1)]
    print(random_word)
    user_input = input("Type " + random_word + ": " )

    for word in word_list:
        if user_input.lower() == word.lower():
            print("Correct! You typed a word correctly.")
            word_list.remove(random_word)
            return True

    print("Incorrect! Try again.")
    return False

while True:
    check_user_input()
