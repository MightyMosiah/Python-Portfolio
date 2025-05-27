#Daniel Brookins
#1/6/25
#Rock Paper Scissors

#Init
import random
wins= 0
losses= 0
ties = 0
#Functions
#Main

print("Welcome to Rock, Paper, Scissor")
while True: #infinite Loop
    #Player's Choice

    print("Please select one of the three options")
    player = input("Selection: ")

    #Computer's Choice

    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("Computer chose rock")

    elif computer == 2:
        computer = "paper"
        print("Computer Chose paper")

    else:
        computer = "scissor"
        print("Computer Chose scissor")

    if  player =="paper"and computer == "rock":
        print("Player wins!")

    elif player =="rock" and computer == "paper":

        print("Computer Wins!")

    elif player == "rock" and computer == "scissor":
        print("Computer Wins!")

    elif player == "scissor" and computer == "paper":
        print("Player Wins!")

    elif player == "paper" and computer == "paper":
        print("Tie Game!")

    elif player == "scissor" and computer == "scissor":
        print("Tie Game!")

    elif player== "scissor" and computer == "rock":
        print("Computer Wins!")
    elif player == "rock" and computer == "rock":
            print("Tie Game!")

    #Ask player if they want to continue
    playagain = input("Would you like to play again?")
    if playagain== "yes":
         print("Restarting....")
    elif playagain == "no":
        break

#Determine the outcome
# = gets the value of
# == is equal to
