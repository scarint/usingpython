# http://usingpython.com/python-file-handling/

# Remember the "double or quit" program we created earlier? See if you can add to the program,
# to save the highest score to a text file, along with the name of the person who acieved the
# score.

# As you're only saving one score/name, you can use "w" to write over the file if a new high score
# is achieved. Before you start developing your program, create a file called "score.txt" with the
# following line in it:

# 0: No Name

# Also, as you only need to read on line from the file, you can use "realine" instead of
# "readlines"

import random

score = 1
play = 'd'

file = open("score.txt", "r")
highScore = file.readline()
file.close()

highScoreName = highScore.split(": ")[1]
highScore = int(highScore.split(":")[0])

print("Current high score: " + str(highScore) + " by " + highScoreName)

while play.lower() == 'd':

    print("\nScore: " + str(score))
    play = input("\nDouble or Nothing? [d/N]")

    if play.lower() == 'd':
        fate = random.randint(0,5)
        if fate == 0:
            score = 0
        else:
            score = score * 2
            if score > highScore:
                highScoreName = input("New high score! Enter your name. ")
                highScore = score
        print("Score: " + str(score))
    if score == 0:
        play = 'q'

data = str(highScore) + ": " + highScoreName
file = open("score.txt", "w")
file.write(data)