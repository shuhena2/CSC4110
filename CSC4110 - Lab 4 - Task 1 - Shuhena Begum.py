#Shuhena Begum
#CSC 4110
#2-7-24

import random
import uuid

#This is the data collector simulating user records with the following attributes: username, password, birthdate, address, social security number, product purchased,and salesperson.
def My_Data_Collect():
    rand_user_Name = ["Nick", "Olivia", "Jacky", "Rachel", "Mason", "Katy", "Leon", "Ava", "Alex"]
    rand_Password = ["Kitty321", "Day0207", "Super862", "LazyRat126","Timber312"]
    rand_birthdate = ["2/7/1900", "3/12/2000", "4/16/2012", "5/24/2014", "6/4/2016"]
    rand_address = ["123 Maple St", "284 Main St", "643 Wayne St", "732 Riverview St", "543 Wall St"]
    rand_social_security = ["541-233-7612", "314-596-2453", "712-548-9749", "649-723-9367", "213-659-3108"]
    rand_product_Purchased = ["ID-pro638", "ID-pro294", "ID-pro762", "ID-pro548", "ID-pro854"]
    rand_sales_person = ["Luis", "Mark", "Sam", "Lucus", "Mike"]
    
    #Here is an empty list where every data is stored 
    stored_user_list = []
    
    #Here it chooses random username, password, birthdate, address, social security number, productPurchased,and salesperson from the random list I have created.
    for i in range(10): 
        random_records = {
            "Username": random.choice(rand_user_Name),
            "Password": random.choice(rand_Password),  
            "Birthdate": random.choice(rand_birthdate),
            "Address": random.choice(rand_address),
            "Social security": random.choice(rand_social_security),
            "Product Purchased": random.choice(rand_product_Purchased),
            "Sales Person": random.choice(rand_sales_person)}
        stored_user_list.append(random_records)
    return stored_user_list

#Here it gets fed the data collectors values into key-value pairs.
def Value_pairs(stored_user_list):
    userData = {}
    for j in stored_user_list:
        user_ID_key = str(uuid.uuid4())  #Here it generates a random Universally Unique Identifier(uuid.uuid4) for a Unique user id key from the python library
        userData[user_ID_key] = j
    return userData

#Here the key-values are searchable
def search_address(stored_user_list, specific_address):
    my_user = []
    for k in stored_user_list.values():
        if specific_address in k["Address"]:
            my_user.append(k)
    return my_user

#The main fuction generates every fuction created from above
if __name__== "__main__":
    #Here is genereates the user data collected by the data collector
    userRecord = My_Data_Collect()
    
    #Here is genereates the key/value pairs collected by the data collector
    user_data_store = Value_pairs(userRecord)
    
    #Here it searches for people in at Maple St
    address_search = "Maple St"  #users can change the string to another address if they are looking for someone there for instance they can change it to Wall St.
    my_user = search_address(user_data_store, address_search)
    
    #Here it prints out the people who are in "Maple St" or a destination a user searches for
    for l in my_user:
        print(l)
