#Shuhena Begum
#CSC 4110
#2-7-24

#Here the random module is imported from the python library
import random

#Here is the fuction that populates the treasure chest with as many items
def TreasureChest(item_amount):
    #In this empty list, everything is being stored in there.
    my_treasureChest = []
    
    #Here is the treasures in the chest with many items.
    my_treasures = ["Diamond", "Gold Coins", "Pearls", "Gold", "Crystals", "Silver", "Gemstones","Ivory"]
    
    #The items in the my_treasures list are chosen at random. 
    for i in range(item_amount):
        my_treasureChest.append(random.choice(my_treasures))
    return my_treasureChest
    
#This is the main fuction that runs the whole program. 
def pirate_Captin_JackSparrow(item_amount):
    #The integer 10 represents the bank balance
    my_Bank_balance = 10
    
    #Prints out a welcome message.
    print("Welcome to Jacks Treasure Quest!")
    
    #Here it states how much is in the users bank account.
    print("In your bank account, you have", my_Bank_balance, "coins.")
    my_treasureChest = TreasureChest(item_amount)
    
    #Here the customer “plays” until bank account reaches 0 or below
    while my_Bank_balance > 0:
        #Here it prints out random items from the Treasure Chest each time the user plays.
        print("Items inside the treasure chest:", my_treasureChest)
        
        #Here it allows the user to choose how many items they want to grab from the treasure chest
        My_Wager = int(input("How many items would you like to grab? "))
        
        #Once the balance hit zero it ends the program
        #It also lets the user know how much their bank balance is each time until it hits zero and ends.
        #Loses 1 coin each time user grabs an item
        if My_Wager > 0:
            my_Bank_balance -= 1
            print("Your bank balance is: ", my_Bank_balance)
       

#The integer 7 represents the number of items in the treasure chest that will chosen at random.
#So, 7 random items get picked from the treasure chest.
#For instance, if the user plugs in the number 2 then only 2 out of the random items will be shown on the screen.
TreasureChest(7)

#The integer 8 in this case is the number of items that populates the treasure chest. 
pirate_Captin_JackSparrow(8)
print("Thanks for playing! Goodbye!")
