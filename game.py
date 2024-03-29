import random

flag = True
guesses = 0
best = 0

def menu():
    print("Welcome to 'Higher or Lower'")
    print("1- Default 2- Custom")
    choice = int(input())
    if choice == 1:
        lower = 0
        higher = 100
    elif choice == 2: 
        lower = int(input("Set the smallest number: "))
        higher = int(input("Set the highest number: "))
    randomNumber = random.randint(lower,higher)
    guess(guesses, randomNumber, lower, higher)

def bestScore(best, amount):
    if not best:
        best = amount
        return best
    elif best > amount:
        best = amount
        return best
    else:
        pass
def playAgain():
    choice = input("Do you want to play again? (Y/N) ").upper()
    if choice == "Y":
        menu()
    else:
        exit()

def validNumberCheck(guess, lower, higher):
    if guess > higher or guess < lower:
        print("Not in range")

def guess(noOfGuesses, randomNumber, l, h):
    flag = True
    while flag:
        guess = int(input("Guess a number: "))
        validNumberCheck(guess,l,h)
        if guess > randomNumber:
            print("Lower")
        elif guess < randomNumber:
            print("Higher")
        else:
            print("You win!")
            flag = False
            playAgain()
        noOfGuesses = noOfGuesses + 1
        print("Number of guesses: ", noOfGuesses)
        print("Best score: ", bestScore(best, noOfGuesses))
menu()