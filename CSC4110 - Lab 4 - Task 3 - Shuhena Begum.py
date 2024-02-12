#Shuhena Begum
#CSC 4110
#2-7-24

#Random module gets imported
import random
#string module gets imported to use the ascii letters, digits, and special characters.
import string

#This is for the sonification and visualization portion for the csv file
import pandas as pd
import csv


#Words in the dictionary list that cannot be used in password. 
#These words in the dictionary are well known passwords that are easy to figure out. 
myDictionary = ["welcome", "password", "user", "login", "trust", "admin", "hello"]

#Here it stores the words in my dictionary as unaccepted password
unacceptedPass = myDictionary

def my_password():
    #Here it creates random passwords with letters, digits, and special symbols.
    acceptedCharacters = string.ascii_letters + string.digits + string.punctuation
    
    #Here it take the accepted characters and makes a random password with 10 characters.
    #8-10 is the best length to have for a password.
    #If the length is short, users can easily get hacked.
    randPassword = "".join(random.choice(acceptedCharacters) for _ in range(10))
    return randPassword

#Here is an empty string that stores all the accepted strings.
#If password is "acceptable," it gets archived.
acceptPass = []

countIteration = 0

#Here the program keeps running until it finds 40 acceptable passwords.
while len(acceptPass) < 40:
    #Here random passwords get generated
    randomPass = my_password()
    #Here iteration goes up by one until it hits 40 and ends the program
    countIteration += 1
    
    #Here it checks if the password is not in the dictionary.
    #It also contains special symbol
    if randomPass not in myDictionary and any(charac in string.punctuation for charac in randomPass):
        acceptPass.append(randomPass)

#Here it prints out the random passwords that were accepted.
print("Passwords that are Accepted:")
for randomPass in acceptPass:
    print(randomPass)
    
#Here "unaccepted" passwords get deleted. These are the words from my dictionary
del unacceptedPass

print('\n')
print("This is part of the visualization that shows the words from my dictionary!")
#Here it reads my CSV file and it has every word from my dictionary
my_visualization = pd.read_csv("myDictionary.csv")

#Here it prints out the words from my dictionary
print(my_visualization.head(6))
