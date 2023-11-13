import random
wordbank = ["LAMANITES", "BRETHREN", "WILDERNESS", "FATHER", "COMMANDMENTS", "VINEYARD", "WICKEDNESS", "MULTITUDE", "CHILDREN", "ZARAHEMLA"]

incorrect_guesses = []
correct_guesses = []

incorrect_amount = 0
correct_amount = 0

#Initialize and start the game
def main():
    word = initializeGame()

    newRound(word)

#Displays the gallows, guess amount, and takes and processses the new guess
def newRound(word):
    global incorrect_amount
    global correct_amount
    drawGame()

    expanded_word = []
    expanded_word.extend(word)

    for char in expanded_word:
        if correct_guesses.__contains__(char):
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("\n " + str(correct_amount + incorrect_amount) + " guesses     " +
           str(correct_amount) + " correct     " + str(incorrect_amount) + " incorrect")

    new_guess = input("Please enter your new guess:\n")

    new_guess = new_guess[0]
    new_guess = new_guess.upper()
    if not new_guess.isalpha():
        print("That guess is invalid, I'll let you try again")
        newRound(word)
        return
    if correct_guesses.__contains__(new_guess) or incorrect_guesses.__contains__(new_guess):
        print("You already guessed that! Try again.")
        newRound(word)
        return

    if expanded_word.__contains__(new_guess):
        correct_guesses.append(new_guess)
        correct_amount += 1
    else:
        incorrect_guesses.append(new_guess)
        incorrect_amount += 1
    

    if incorrect_amount >= 6:
        loseScreen()
    elif correct_amount >= len(set(expanded_word)):
        winScreen()
    else:
        newRound(word)

#Congratulates the player for winnings and asks if they want to try again
def winScreen():
    drawGame()
    global incorrect_amount
    global correct_amount
    print("\n\n Congratulations! You correctly guessed the word in " + str(incorrect_amount + correct_amount) + " guesses.")
    print("Bob has survived this time.")
    again_prompt = input("Would you like to try again? (enter yes or no)\n")
    again_prompt = again_prompt.lower()
    if not again_prompt.isalpha():
        print("That answer is invalid, try again")
        winScreen()
    if again_prompt == "yes":
        main()
    else:
        print("Thank you for playing!")
        return
    
    
#Shows the player that they lose and asks if they want to try again
def loseScreen():
    drawGame()
    print("Ouch! As you can see Bob is dead. However there's more where he came from. \nYou Lose.")
    again_prompt = input("Would you like to try again? (enter yes or no)\n")
    again_prompt = again_prompt.lower()
    if not again_prompt.isalpha():
        print("That answer is invalid, try again")
        winScreen()
    if again_prompt == "yes":
        main()
    else:
        print("Thank you for playing!")
        return

#Prepares the variables for a new game and prints instructions
def initializeGame():
    index = random.randint(0, 9)
    word = wordbank[index]
    global incorrect_guesses
    global correct_guesses
    global correct_amount
    global incorrect_amount
    incorrect_guesses = []
    correct_guesses = []
    correct_amount = 0
    incorrect_amount = 0

    print("Welcome to a friendly game of Hangman!")
    print("Your job is to guess all the letters in a word that I have chosen before I finish hanging Bob.")
    print("When you guess a letter correctly, it will reveal in the word.")
    print("When you are incorrect, I will continue hanging Bob.")
    print("After 6 incorrect guesses I will be finished hanging Bob and you will lose.")
    #print("The word is " + word)

    return word

#Returns a string of all the incorrect guesses
def strIncorrectGuesses():
    output = ""
    for guess in incorrect_guesses:
        output = output + guess + " "
    return output

#Draws up the gallows and Bob according to the incorrect guesses
def drawGame():
    print("\n")
    print("    ________")
    print("    |      |      " + strIncorrectGuesses())
    print("    |      ", end="")
    if incorrect_amount > 0:
        print("O", end="")
    if incorrect_amount == 2:
        print("\n    |      |")
    elif incorrect_amount == 3:
        print("\n    |     /|")
    elif incorrect_amount > 3:
        print("\n    |     /|\\")
    else:
        print("\n    |")
    print("    |     ", end="")
    if incorrect_amount > 4:
        print("/", end=" ")
    if incorrect_amount > 5:
        print("\\", end=" ")
    print("")
    print("    |")
    print("")
    

#print("    ________")
#print("    |      |   A B C D E F)
#print("    |      O")
#print("    |     /|\")
#print("    |     / \")
#print("    |")

#runs the main function
main()