import os
import words

word_list = words.generate_random_words(10)                             # Generate a list of 10 random words
length_words = len(word_list)                                           # Declare a variable to keep track of length of words generated
count = 0                                                               # Initialize count
centered_arrow = "=>".center(-40)                                       # Center arrow for user input

def check_user_input():
    global count, score                                                 # Declare count as global variables
    if count <= length_words - 1:                                       # Check if list of words has not finished
        word = word_list[count]                                         # Choose a word from the list of words (First word will be at index 0 of the list) 
        print("**************************************")
        if os.name == 'nt':
            os.system('cls')                                            # Clear terminal to keep interface clean
        print("******************************************")
        print(f"{word.center(40)}")                                     
        print("******************************************")
        user_input = input(centered_arrow)                              # Request user input
        print("**************************************")
        word_lower = user_input.lower()                                 # Convert user input into a string containing only lowercase
        if word_lower in word_list:                                     # Check if users input is in word_list
            count += 1                                                  # If it is move onto the next word
            return True                                                 
        print("Incorrect! Try again.")                                 # If not then index will stay the same and word as well, reprompt user for same word
        return True
    else:
        print("Thank you for typing!!!")                               # When we finish through the whole list of words print thank you message
        return False