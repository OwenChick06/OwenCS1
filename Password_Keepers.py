import random #imports library
import string #imports library

characters = 'qwertyuiopasdfghjklzxcvbnm1234567890' #list of characters for the password generator to draw from
 
websites = [] #websites list
usernames = [] #usernames list
passwords = [] #passwords list

'''
    #Prompt to ask user for website, username, and password

    #Returns:

        #username, website, password into designated list

    #Extraneous (Raises/Prints etc.):

        #Prints: the prompts for the user to enter their information
    '''
def prompt(): 
    website = input("please enter a website: ") #prompts user to enter website
    username = input("please enter a username: ") #prompts use to enter username
    pass_choice = input("would you like to choose a password (1) or generate random (2) one?: ") #asks user if they would like a random password
    if pass_choice == "1": #if user input is 1
        password = input("please enter a password: ") #promts user to enter a password
    else:
        for y in range(1): #how many passwords will it generate
            password = ''
            for x in range(8): #how long will the password be
                password += random.choice(characters) #generates the password

    websites.append(website) #appends list with user input
    usernames.append(username) #appends list with user input
    passwords.append(password) #appends list with user input

prompt() #runs the funtion 'prompt'

while True: #forever loop
    
    '''
    #Prints all of the lists

    #Extraneous (Raises/Prints etc.):

    #Prints: Prints all of the lists in order for the user to view
    '''
    def print_all():

        for i in range(len(websites)): #for every input in websites list
            print(websites[i], usernames[i], passwords[i]) #print the variables that coincide with the websites

    choice = input("would you like to print all (1), print a specific (2), save more passwords (3), or end program (4): ") #prompts the user with multiple options

    if choice == "2": #if user choice is 2
        website_choice = input("what website would you like the password for? ") #prompts the user for specific website
	    
        for website_choice in range(len(websites)): 
            print(usernames,passwords) #print username and password for specific website

    elif choice == "1": #if user choice is 1
        print_all() #runs the funciton
    
    elif choice == "4": #if user choice is 4
        exit() #immidiatly stops the program

    else:
        prompt() #runs the function
