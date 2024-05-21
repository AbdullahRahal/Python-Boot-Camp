import wordlist
import letter_cheking
import random
import check_life
from replit import clear

# Global Variables
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
blanks = 1
guesses = ""
life = 6

# Generate a random number in a range of the wordlist we have
num = random.randint(0, 39)

# choose a word depending on the random number has been generated
chosen_word = wordlist.wordlist[num]

# create a list to represent the blanks in the word
blanks_list = []
for num in chosen_word:
    blanks_list += "_"

print(logo + "\n")
# a loop to run the game while the word still have blanks
while blanks != 0:

    # Reset the guesses word to empty
    guesses = ""

    # ask the user to guess a letter and take that input in lower case
    guess = input("Choose a letter to fill in the blanks: ")
    guess_lower = guess.lower()

    # clear the screen
    clear()

    if guess in blanks_list:
        print("You already guessed that!")
    else:
        # check if the user guess was one of the blanks and print how the blanks looks after this guess
        letter_cheking.checking(guess_lower, chosen_word, blanks_list)

        # check if the user have lives and check if his guess is wrong
        if guess not in chosen_word:
            life -= 1

        # sum the letters in the list to check for the blanks using Count()
        for letters in blanks_list:
            guesses += letters

        # check if the word still have blanks and decide either end the game or not
        if guesses.count("_") != 0:
            blanks = 1
        else:
            blanks = 0
            print("You Win!")

        # check if the life is not = to 0 and if it is end the game
        if life != 0:
            blanks = 1
        else:
            blanks = 0
            print("Out of hearts")
            print("he died!")
        # prints out
        print(logo + "\n")
        print(blanks_list)
        print(check_life.stages[life])
