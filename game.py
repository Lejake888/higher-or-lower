import random

flag = True
randomNumber = random.randint(0,10)

def randomiser():
    guess = int(input("Guess a number: "))
    if guess > randomNumber:
        print("Lower")
    elif guess < randomNumber:
        print("Higher")
    else:
        print("You win!")

while flag == True:
    randomiser()