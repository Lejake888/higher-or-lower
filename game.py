import random

randomNumber = random.randint(0,10)
guess = int(input("Guess a number: "))

if randomNumber < guess:
    print("Higher")
elif randomNumber > guess:
    print("Lower")
else:
    print("You win!")
    flag = False