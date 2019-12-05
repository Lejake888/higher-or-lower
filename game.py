import random

flag = True
noOfGuesses = 0
randomNumber = random.randint(0,100)

def randomiser(noOfGuesses):
    guess = int(input("Guess a number: "))
    if guess > randomNumber:
        print("Lower")
    elif guess < randomNumber:
        print("Higher")
    else:
        print("You win!")
    noOfGuesses = noOfGuesses + 1
    print("Number of guesses: ", noOfGuesses)

while flag == True:
    randomiser(noOfGuesses)