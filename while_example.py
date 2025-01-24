# you have 3 lives, I roll the dice, if I roll 6 you win
# if not a 6, you lose 1 life

from random import randint

lives = 3
while lives: # change lives into True if you want infinite lives
    roll = randint(1, 6) # make sure to not put a: and b:!!
    if roll == 6:
        print("You rolled a 6! You win!")
        break # this exists the wile even if lives still > 0
    # there is no other way to get here, unless i DID NOT roll a 6
    print(f"You rolled a {roll}! You lose a life")
    lives -= 1
    print(f"Lives left: {lives}")
else: # else from while!!
    print("You lost!")
