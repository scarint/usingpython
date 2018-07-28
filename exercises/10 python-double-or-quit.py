import random

score = 1
play = 'd'

while play.lower() == 'd':

    print("\nScore: " + str(score))
    play = input("\nDouble or quit? [D/N]")

    if play.lower() == 'd':
        fate = random.randint(0,5)
        if fate == 0:
            score = 0
            print("Lost")
        else:
            score = score * 2
            print("Win.")
    if score == 0:
        play = 'q'

print("\nFinal Score: " + str(score))
