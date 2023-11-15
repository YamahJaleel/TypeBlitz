import os
import words

def type_blitz(num_words):
    word_list = words.generate_random_words(num_words)      # Generate a list of random words
    length_words = len(word_list)                           # Declare a variable to keep track of the length of words generated
    count = 0                                               # Initialize count
    arrow = "=>"

    def print_separator():
        print("*" * 40)

    def clear_terminal():
        if os.name == 'nt':
            os.system('cls')                                # Clear terminal on Windows (if os is mac or linux must update this line of code accordingly)

    def type_blitz_prompt():
        nonlocal count                                      # Use nonlocal to modify the count variable in the outer function
        if count < length_words:                            # Check if list of words has not finished
            word = word_list[count]                         # Choose a word from the list of words
            print_separator()
            clear_terminal()
            print_separator()
            print(f"{word.center(40)}")
            print_separator()
            user_input = input(f"{arrow.center(12)}")         # Request user input
            print_separator()
            word_lower = user_input.lower()                  # Convert user input to lowercase
            if word_lower == word:                           # Check if user's input matches the current word
                count += 1                                   # Move on to the next word
                return True
            print("Incorrect! Try again.")                   # Reprompt user for the same word
            return True
        else:
            clear_terminal()
            print_separator()
            print("*        Thank you for typing!!!       *")                # Finish through the whole list of words
            print_separator()
            return False

    while type_blitz_prompt():
        pass                                                # Keep prompting until the user finishes or exits