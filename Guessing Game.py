#Daniel Brookins
#11/11/24
#Random Number Genrator
#Int
def game():
    import random
    print("Welcome to Guessing Game")
    difficulty=input("What difuculty Would you like to Play on?")
    if difficulty== "easy":
        secret=random.randint(1,10)
    if difficulty== "medium":
        secret=random.randint(10,20)
    if difficulty== "hard":
        secret=random.randint(20,30)
    for i in range(3):
        print("Guess a Number")
        guess = int(input("Enter Guess"))#String
        if guess== secret:
            print("You Win!")
        else:
            print("loose")
            if guess>secret:
                print("Too High!")
            if guess<secret:
                print("Too Low!")
            print("The secret number was " + str(secret))
            print("Try Again")

#Main
game()
