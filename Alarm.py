import random #imports library "Random"
import sys #imports library "sys"

times = ["6:30","6:40","6:50","7:00","7:10","7:20","7:30", "7:40", "7:50", "8:00", "8:10"]
i = 0 #Creates a library of times, labled "times" and assignes it a value of 0, aka 6:30

    
print ("Alarm") #Prints the word "Alarm"


while True: #Allows the block of code to loop forever
    print("The time is",times[i],"AM") #Prints the text, than the time listed in "times" library relative to the value of i, than prints the rest of the text
    snooze = input("Go back to sleep?") #Asks the user a question

    if snooze == "yes": #Defines and answer for snooze
        print ("Go back to sleep for 10 minutes")
        i += 1 #Adds +1 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
    elif snooze == "no": #Defines and answer for snooze
        print ("Wake up!") #Prints "Wake up" when a user answers No
        i += 1 #Adds +1 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    else: #Gives an alternative answer for snooze	
        print ("Invalid Response") #Prints "Invalid Response", when an answer is not Yes or No
        snooze = input("Go back to sleep?") #Restates the initial question
    
  
while True: #Allows the block of code to loop forever
    print("The time is",times[i],"AM")#Prints the text, than the time listed in "times" library relative to the value of i, than prints the rest of the text
    shower = input("Will you take a shower?") #Asks a yes or no question, labled "shower"

    if shower == "yes":  #Defines and answer for shower
        print ("You are now clean")
        i += 2 #Adds +2 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    elif shower == "no": #Defines and answer for shower
        print ("You feel dirty")
        i += 1 #Adds +1 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    else: #Gives an alternative answer for shower	
        print ("Invalid Response") #Prints "Invalid Response", when an answer is not Yes or No
        shower = input("Will you take a shower?")

while True: #Allows the block of code to loop forever
    print("The time is",times[i],"AM")#Prints the text, than the time listed in "times" library relative to the value of i, than prints the rest of the text
    eat = input("What will I make for breakfast? I have cereal, eggs, and pancakes")#Asks a question regarding breakfast options, labled "eat"

    if eat == "cereal": #Defines and answer for eat
        print ("That was quick")
        i += 1 #Adds +1 to the value of i
        sick = random.randint(1,100) #Makes a random number, 1-100
        if sick > 95: #If the random number is greater than 95, you get food poisoning
            print ("You got food poisoning")
            i += 10 #Adds +10 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    elif eat == "eggs": #Defines and answer for eat
        print ("That took a little while")
        i += 2 #Adds +2 to the value of i
        sick = random.randint(1,100) #Makes a random number, 1-100
        if sick > 90: #If the random number is greater than 90, you get food poisoning
            print ("You got food poisoning")
            i += 10 #Adds +10 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(")#Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    elif eat == "pancakes": #Defines and answer for eat
        print ("That took a long time")
        i += 3 #Adds +3 to the value of i
        sick = random.randint(1,100) #Makes a random number, 1-100
        if sick > 85: #If the random number is greater than 85, you get food poisoning
            print ("You got food poisoning")
            i += 10 #Adds +10 to the value of i
        if i > 9: #If the value of "times" gets above 9 (8:00), than kills the code
            print ("You missed the bus! :(") #Prints "You missed the bus" before the code is killed
            sys.exit()
        break #Breaks the loop
    else: #Gives an alternative answer for eat
        print ("Invalid Response")#Prints "Invalid Response", when an answer is not one listed in the question
        eat = input("What will I make for breakfast? I have cereal, eggs, and pancakes")

while True: #Allows the block of code to loop forever
     print("The time is",times[i],"AM")#Prints the text, than the time listed in "times" library relative to the value of i, than prints the rest of the text
     if i <= 10: #If the value of i is less than or equal to 10, you 'win'
         print("You made it to the bus in time!:)") #Prints "you made it to the bus"
         break #Breaks the loop

