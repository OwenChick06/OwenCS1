"""
Author: Owen Chickering
Date: 11/27/23
Sources: Elijah Murphy
Bugs: None
Purpose: A working game of rock paper scissors
"""


import random #Import random
import sys #Import sys

def scoreboard():
    print("The computer has",cm,"points") 
    print("You have",pl,"points")
    
game = ["rock", "paper", "scissors"] #creates a list titled game, for the playing options

computer = random.choice(game) #Assigns a variable name computer to a random choice from game

player = False #Sets player to false

pl = 0 #Creates variable name PL with a value of 0
cm = 0 #Creates variable name CM with a value of 0

while player == False: #When player is equal to var "false," run the next lines
    player = str.lower(input("Rock, Paper, Scissors?")) #Ask "r,p,c" and awaits a response
    print("Computer chooses", computer) #Prints whatever random.choice is assigned
    if player == computer: #If the variable the computer chose matches the variable the player chose, run the following lines of code
        print("Tie!") #Prints the word Tie!
    elif player == "rock": #If player = rock, prompt the elif statement
        if computer == "paper":#If comp = paper, prompt the if statement
            print("You lose!", computer, "covers", player) #Prints "You Lose" if p = rock and c = paper
            cm += 1 #Adds +1 to the value of "cm"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
        else:
            print("You win!", player, "smashes", computer) #Prints "you win" plus the variables the player and computer chose
            pl += 1 #Adds +1 to the value of "pl"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
    elif player == "paper": #If player = paper, prompt the elif statement
        if computer == "scissors": #If comp = scissors, prompt the if statement
            print("You lose!", computer, "cut", player) #Prints "You Lose" if p = paper and c = scissors
            cm += 1 #Adds +1 to the value of "cm"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
        else:
            print("You win!", player, "covers", computer) #Prints "you win" plus the variables the player and computer chose
            pl += 1 #Adds +1 to the value of "pl"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
    elif player == "scissors": #If player = scissors, prompt the elif statement
        if computer == "rock": #If comp = rock, prompt the if statement
            print("You lose...", computer, "smashes", player) #Prints "You Lose" if p = scissors and c = rock
            cm += 1 #Adds +1 to the value of "cm"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
        else:
            print("You win!", player, "cut", computer) #Prints "you win" plus the variables the player and computer chose
            pl += 1 #Adds +1 to the value of "pl"
            scoreboard()
            repeat = input("Do you want to play again?").lower() #Prints "again" and waits for a response
            if repeat == "yes": #If response is yes, trigger the if statement
                player = False #Sets player to false
            else: #If the response is anything but yes, run the next line(s)
                sys.exit() #Stops the program
    else:
        print("Invalid Response") #Prints "Invalid Response"
    player = False #Sets player to false
    computer = random.choice(game) #Makes computer choose random value from list 


    





