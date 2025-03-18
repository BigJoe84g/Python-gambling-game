import random as ran

#Funny gambling game for dumb dumbs

cash = 200  #Cash for the player, changes through play
print("You currently have " + str(cash) + " dollars!")  #Prints how much money the user has
game = input("What game do you want to play, dice or roulette?")    #asks the user what they want to play?
def dice(cash):
    bet = str(input("How much money do you want to wager?")) #Player bet
    roll = str(input("Say 'Roll!' to roll your dice!")) # Collects the user 'Roll!' input
    if roll == "Roll!": #Checks if the user said roll, if they did the following code is executed
        playerdice = ran.randint(1,6)   #Creates a random dice roll using the random library
        playerdice2 = ran.randint(1,6)  #Creates a second random dice roll using the random library
        print("You rolled a " + str(playerdice) + " and a " + str(playerdice2))     #Tells the user what they rolled
        print(playerdice+playerdice2)   #Adds the two player's dice together
    print("The computer will now match your bet and roll the dice!")    #The computer matches the player's bet and rolls their dice
    dice = ran.randint(1,6)     #The computer's first dice is generated
    dice2 = ran.randint(1,6)    #The computer's second dice is generated
    print("The computer rolled a " + str(dice) + " and a " + str(dice2))    #Tells the user what the computer rolled
    print(dice+dice2)   #Adds the computer's dice together
    if dice+dice2 > playerdice+playerdice2:     #Checks if the computer's dice numbers are greater than the user's dice.
        print("The computer won!")  #If the computer wins, it prints a message saying the computer won
        cash = cash - int(bet)  #Updates the user's remaining cash
        print("You have",cash, " !")    #Prints how much cash the user has remaining
    elif playerdice+playerdice2 > dice+dice2:   #If the player's dice is greater than the computer's dice, the player wins
        print("The player won!")    #Prints that the player won
        cash = cash + int(bet)      #Updates the player's cash if they win
        print("You have",cash, "cash!")     #Tells the user how much cash they have left
    elif playerdice+playerdice2 == dice+dice2:      #If the player and the computer roll the same thing, the program terminates
        print("You both rolled the same thing, it is a push!")      #Prints information to the user telling them if it's a push
        quit()  #Quits the program if the player and the computer have the same numbers
    else:   #If something else happens the program terminates itself
        print("The program has crashed!")
        quit()
    return cash     #Returns the cash variable to update it
def roulette(cash):
    print("Welcome to roulette!")
    bet = str(input("How much money do you want to wager?"))
    color = str(input("What color do you choose, red or black?"))
    colorList = ["black", "red"]
    randomColor = ran.choice(colorList)
    if randomColor == color:
        print("You got the correct guess!")
        cash = cash + int(bet)
        print("You have",cash, "cash!")
    elif randomColor != color:
        print("You didn't guess correct!")
        cash = cash - int(bet)
        print("You have",cash, "cash!")
    else:
        print("An error occured!")
        quit()
if game == "dice":
    dice(cash)
elif game == "roulette":
    roulette(cash)