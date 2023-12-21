import os
import time
import type

if __name__ == "__main__":
    
    #Clear the Terminal 
    os.system('cls' if os.name == 'nt' else 'clear')  

    # Initalize intro text to be printed
    lines = [
        "*" * 65,
        "*          💻          Welcome to TypeBlitz !        💻         *",
        "*               Your mission is clearly defined                 *",
        "*     Type the word displayed on the screen and press ENTER     *",
        "* If you get it wrong, brace yourself for a relentless reprompt *",
        "*" * 65,
        ""
    ]

    # Print string with a delay
    def print_with_delay(text, delay=0.025):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

    # Print input string with delay
    def input_with_delay(prompt, delay=0.025):
        print_with_delay(prompt, delay)
        user_input = input()
        return user_input   
    
    # Print intro text with a delay
    for line in lines:
        print("\n")
        print_with_delay(line)

    #Ask User for how many words to generate
    num_words_to_generate = int(input_with_delay("Enter how many words to type: "))

    # Instantiate the type_blitz object within the type class
    type.type_blitz(int(num_words_to_generate))                            