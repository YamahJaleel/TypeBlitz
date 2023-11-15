import os
import type

if __name__ == "__main__":
    
    if os.name == 'nt':
        os.system('cls')  
    
    print("*" * 65)
    print("*                    Welcome to TypeBlitz !                     *")
    print("*               Your mission is clearly defined                 *")
    print("*     Type the word displayed on the screen and press ENTER     *")
    print("* If you get it wrong, brace yourself for a relentless reprompt *")
    print("*" * 65)
    print("")

    num_words_to_generate = input("Enter how many words to type: ")
    user_input = input("Press ENTER if you are ready ")

    type.type_blitz(int(num_words_to_generate))                            