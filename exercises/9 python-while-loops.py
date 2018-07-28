import random

play = 'y'

while play.lower() == 'y':

    print("\nDid you win?")

    for goes in range(5):
        fate = random.randint(0,1)
        if fate == 0:
            print("No. Loser.")
        else:
            print("Yes. But not because of anything you did.")
    play = input("Do you want to play again? (Y/n)")