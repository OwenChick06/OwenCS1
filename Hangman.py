import random #brings random library for use in coe

#creates list of hangman pics
hangman_pics = ['''              
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = ["greetings","zebra","school","coffee","morning","snow","summer","water","tadpole"] #possible words for player to be assigned to 
secret = random.choice(words) #sets secret to a random word from the words list
secret_list = list(secret) #breaks secret word into independent characters
hidden = [] #create and empty list
guesses = 0 #creates variable to keep track of guesses

for character in secret_list: #
    if character == " ": #if character is space
        hidden.append(" ") #adds a space instead of _ if word(s) from word list have a space
    else: #otherwise
        hidden.append("_ ") #turns every letter from secret into _ (except for spaces)
        
print("".join(hidden)) #converts hidden list into string to be displayed

while "_ " in hidden and guesses < len(hangman_pics) - 1: #will loop if there are still _ and there are more hangman pictures
    print(hangman_pics[guesses]) #prints hangman picture
    
    while True: #if true, run code below
        guess = str.lower(input("Enter a letter: ")) #asks for player go guess a letter, and makes it lowercasr

        if guess not in list("abcdefghijklmnopqrstuvwxyz "): #demands answer to be letter
            print("Please ender a letter!") #displays text
        else: #otherwise
            break #end while true loop
        
    if guess in secret_list: #if the player chooses a letter thats in the random word
        for index in range(len(secret_list)): #runs loop for each _ in the random word
            if guess == secret_list[index]: #if player picks a letter in the random word
                hidden[index] = guess #converts _ into the letter the player guessed
        print("".join(hidden)) #converts hidden list into string to be displayed
    else: #otherwise
        print("Not here!") #prints that the letter picked isnt in the random word
        guesses += 1 #adds +1 to how many tries it took player
        print(hangman_pics[guesses]) #prints image that corrisponds to how many tried it took the player

if "_ "  in hidden:
    print(f"You lost! The word was {secret}")
else:
    print("You won!")



