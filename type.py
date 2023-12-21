import os
import words
import time

def type_blitz(num_words):
    word_list = words.generate_random_words(num_words)      # Generate a list of random words
    length_words = len(word_list)                           # Declare a variable to keep track of the length of words generated
    count = 0                                               # Initialize count
    arrow = "=>"

    # Print Separator
    def print_separator():
        print("*" * 40)

    # Print string with a delay
    def print_with_delay(text, delay=0.025):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

    # Clear the Terminal depending on operating system
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')    

    # Prompt User to input a word and check if input is correct
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
            print_with_delay("*" * 45)
            print_with_delay("\n*    🫡    Thank you for typing!!!    🫡    *")                # Finish through the whole list of words
            print_with_delay("\n" + "*" * 45)
            time.sleep(3)
            clear_terminal()
            return False

    # Keep prompting until the user finishes or exits
    while type_blitz_prompt():
        pass                                                 