import time
import keys

def typing_test():

    word_to_type = words.generate_random_word()

    print("Type the following word: {}".format(word_to_type)

    start_time = time.time()

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if user_input == word_to_type:
        print("Congratulations! You typed the word correctly.")
        print("Time taken: {:.2f} seconds".format(elapsed_time))
    else:
        print("Oops! Incorrect typing. Try again.")

if __name__ == "__main__":
    while True:
        typing_test()
