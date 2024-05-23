# Author: Owen Chickering
# Date: 3/28/24
# Project Goal: Creates a menu with corrisponding letter/number codes for the user to choose from, or the user can select random and they will be givin a possibly infinate combination of recipes
# Sources: Teacher Help, Google Classroom

import random #imports library random

primaries = ["cauliflower","tilapia fillet","pork loin","green beans","rainbow carrots","potatoes","three color squash","eggplant","eye round of beef","baguette"]
letters = ["A","B","C","D","E","F","G","H","I","J"]
secondaries = ["with balsamico","with garlic and olive oil","with minted yogurt","soup","chutney","salad","with salsa","over sticky rice","au jus","with basmati rice"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
#all of these above are lists with corrisponding letters/numbers
choice = input("Random or Select? ") #promts the user to select random or select

if choice == "Random": #if user types random then
    number_of_items = int(input("How do many items do you want? "))#asks the user for a number which decides how many items they want

    for i in range(number_of_items):#for how many items the user wants
        primary = random.choice(primaries)#defines random choice of primary
        secondary = random.choice(secondaries)#defines random choice of secondary
        print(f"{primary} {secondary}, this is {letters[primaries.index(primary)]}{numbers[secondaries.index(secondary)]}")#prints list of random menu items and how many the user wants, in edition to the corrisonding letter/number code
elif choice == "Select":#if the user chose select
    for i in range(len(primaries)): #for the range of primaries
        print(f"{primaries[i]}, {letters[i]}")#prints all of the primarys with their corrisponding letter
    for i in range(len(secondaries)):#for the range of secondaries
        print(f"{secondaries[i]}, {numbers[i]}")#prints all of the secondaries with their corrisponding number

    selection = input("What dish would you like? ")#prompts the user for a number/letter code
    letter = selection[0] #defines selection to letter 
    number = selection[1] #defines selection to number
    print(f"{primaries[letters.index(letter)]} {secondaries[numbers.index(number)]}")#prints the users selection
else:#if the user entered something else
    print("Please either input 'Random' or 'Select'")#re prompt the user with select or choice        
