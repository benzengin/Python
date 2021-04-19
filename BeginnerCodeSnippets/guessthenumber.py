from random import randrange

userPoints = 0
computerPoints = 0
counter = 0

while(counter < 10):

    computerNumber = randrange(1,3) # this will return a number from 1 - 2

    userGuess = str(input("Guess the number from 1 - 2, what is the number? : ")) 

    if userGuess == str(computerNumber):
        print("Awesome: You got it right :)")
        userPoints = userPoints + 1
    elif userGuess != computerNumber:
        print("Wrong, try again.")
        print("The correct answer was: " +str(computerNumber))
        computerNumber = computerNumber + 1

    counter = counter + 1

# the result --> we want to execute this only once

if(userPoints > computerPoints):
    print("You won.")
    print("You got " +str(userPoints)+ " points")
else:
    print("You lost.")

# Computer will select a random number from 0 - 10
# User has to guess which number computer selected
# If user's guess is correct --> user gets a point
# If user's guess is incorrect --> computer gets a point

