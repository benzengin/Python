from random import randrange

print("THIS IS THE BORED ADMIN GAME :)")
options = ["rock","paper","scissor"]

userPoints = 0
computerPoints = 0

counter = 0
rounds = 3

while(counter < rounds):

    computerChoice = options[randrange(len(options))] 

    userChoice = str(input("What is your choice: rock, paper, scissor? : "))


    if userChoice == "rock":
        if computerChoice == "scissor":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("You got a point!")
            print("")
            userPoints = userPoints + 1
        elif computerChoice == "paper":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Computer got a point :( ")
            print("")
            computerPoints = computerPoints + 1
        elif computerChoice == "rock":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Draw!")
            print("")
        else:
            pass

    elif userChoice == "paper":
        if computerChoice == "scissor":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Computer got a point!")
            print("")
            computerPoints = computerPoints + 1
        elif computerChoice == "rock":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("You got a point!")
            print("")
            userPoints = userPoints + 1
        elif computerChoice == "paper":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Draw!")
            print("")
        else:
            pass

    elif userChoice == "scissor":
        if computerChoice == "paper":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("You got a point!")
            print("")
            userPoints = userPoints + 1
        elif computerChoice == "rock":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Computer got a point :( ")
            print("")
            computerPoints = computerPoints + 1
        elif computerChoice == "scissor":
            print("")
            print("You: " + userChoice.upper() + " computer: " + computerChoice.upper())
            print("")
            print("Draw!")
            print("")
        else:
            pass

    else:
        print("Please select your object!")

    counter = counter + 1 

print("*************************************")
print("******* You got a total of: " + str(userPoints))
print("******* Computer got a total of: " + str(computerPoints))    
if(userPoints > computerPoints):
    print("You won!")
elif (computerPoints > userPoints):
    print("Hal Sieg :( ")
    print("GAME OVER, You LOST!")
else:
    print("******** Draw No One Wins")
