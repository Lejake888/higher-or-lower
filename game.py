import random

flag = True
guesses = 0

def menu():
    choice = int(input("Welcome to 'Higher or Lower': 1- Default 2- Custom "))
    if choice == 1:
        randomNumber = random.randint(0,100)
    elif choice == 2: 
        randomNumber = setUp()
    guess(guesses, randomNumber)

def setUp():
    lower = int(input("Set the smallest number: "))
    higher = int(input("Set the highest number: "))
    randomNumber = random.randint(lower,higher)
    return(randomNumber)

def guess(noOfGuesses, randomNumber):
    flag = True
    while flag:
        guess = int(input("Guess a number: "))
        if guess > randomNumber:
            print("Lower")
        elif guess < randomNumber:
            print("Higher")
        else:
            print("You win!")
            flag = False
        noOfGuesses = noOfGuesses + 1
        print("Number of guesses: ", noOfGuesses)

menu()