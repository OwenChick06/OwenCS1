# Owen Chickering
# 4/23/24
# No known bugs
# No outside help


import random #imports random library

def verse_1(): #defines a function
    print("Happy Birthday To You!") #prints happy birthday verse
def verse_2(): #defines a function
    print("Happy Birthday To You!") #prints happy birthday verse
def addition(number1, number2): #defines a function
    print("Number 1:", number1) #prints numbers
    print("Number 2:", number2) #prints numbers
    addition = number1 + number2 #adds the two numbers together
def print_list(my_list): #defines a function
    for element in my_list:
        print(element) #prints element
def missing(numbers,numlist): #defines a function
    return numbers in numlist
def check_int(inputnumber): #defines a function
    try: #trys code
        inputnumber = int(inputnumber) #turns inputnumber into an int
        return True #if code works retrun true
    except ValueError:
        return False #if code fails with a value error return false
def number(): #defines a function
    inputnumber = input("Enter Number") #asks the user to enter a number 
    print(check_int(inputnumber)) #checks if the input is actually a number
def get_random_number(): #defines a function
    while True: #while it is true
        number1 = input("Enter a Number ") #asks user for a number
        number2 = input("Enter another Number ") #asks user for another number

        if check_int(number1)and check_int(number2): #if both inputs are numbers
            print(random.randint(int(number1), int(number2)))
            break #breaks while true

        else: #if is something else
            print("That is not a number!") #print statement
def character_replace(string,old_character,new_character): #defines a function
    new_string = ""

    for character in string: #for every character in string
        if character == old_character: #if a character in the word is defined as an old character
            new_string += new_character
        else:
            new_string += character #new string + old characters 
    return new_string #retu
def main(): #defines a variable to call on every funcion
    verse_1() #calls on function
    verse_2() #calls on function
    add = addition(4,9) #calls on function
    print(add) #calls on function
    foods = ["apple","pear","orange"] #calls on function
    print_list(foods) #calls on function
    print(missing(2,[1,2,3,5])) #calls on function
    number() #calls on function
    get_random_number() #calls on function
    print(character_replace("hello","l","i"))

main() #calls on all of the functions
