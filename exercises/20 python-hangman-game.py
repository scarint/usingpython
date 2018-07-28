import random
import pickle

file = open("hangmanwords.txt", "r")
selected = False
play = True
word = ""

while selected == False:
# method from https://stackoverflow.com/questions/2081836/reading-specific-lines-only-python
    choice = random.randint(0,1000) + 1
    with open("hangmanwords.txt") as fp:
        for i, line in enumerate(fp):
            if i == choice:
                word = fp.readline()
    if word != "":
        selected = True

guess = []      # List to contain guesses
letter = 'a'    # Initialize
tries = int(input("How many tries would you like? "))
guesses = 0

#print(word)    # Debug

while play == True:
    for ch in word:                 # Display word with blanks
        if ch in guess:
            print(ch, end=" ")
        else:
            if ch != '\n':          # Ignore the newline character at the end
                print("_", end=" ")
    print("\n")

    guessAgain = True               # Keep guessing until a new character is chosen
    while guessAgain == True:
        letter = input("Enter a character: ")
        if letter not in guess:     # New letter guessed
            guess.append(letter)    # Add to guess list
            guessAgain = False      # Quit loop
            guesses += 1            # Increment guess count

    if letter not in word:          # Check if the guessed letter is in the word
        print(letter + " is not in the word.")
    else:
        print(letter + " is in the word.")

    print (str(tries - guesses) + " guesses remaining.")

    if guesses >= tries:            # Check if player has exceeded the number of tries
        print("Lost. The word was " + word)
        play = False

    letter = ""                     # Reset for next iteration

#    print("Guesses: ") # Debug
#    print(guess) # Debug

    correct = 0
    for ch in word:                 # See how many letters have been correctly guessed
        if ch in guess:
            correct += 1

#    print("Correct letters: " + str(correct))  # Debug
#    print("Lenght of word: " + str(len(word))) # Debug

    if correct == (len(word) - 1):      # Ignore the newline character at the end
        print("Congratulations, you've guessed the word, " + word + ", you win!")
        play = False
