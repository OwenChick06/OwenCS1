"""
Author:Owen Chickering
Date:11/7/23
Sources: The slideshow
"""
import random #imports library lables random
ball=["yes","no","maybe","ask again later"] #makes a list of random variables labled "ball"
randball = input("I am a magic 8 ball, ask me anything") #asks a question in which the user can type whatever they want
print (random.choice(ball)) #prints a random choice from "ball"
