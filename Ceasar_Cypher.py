#Encryption
#Manav Shardha
#Ceaser Cypher

import time

x = input("Enter a string to encode: ")
character_dictionary = {}
k_thanks = []
unscrambled = []
n = len(input("Please enter a 4 digit password: "))
        

for character in x:
    y = ord(character)
    z = y-2
    scrambled = chr(z)
    k_thanks.append(scrambled)
    scrambled_message = ''.join(k_thanks)
    unscrambled.append(chr(z+2))
    unscrambled_message = ''.join(unscrambled)


    
print(k_thanks)
print("\n\n\n\n\n\n\n")
print(scrambled_message)
print("\n\n\n\n\n\n\n")
print(unscrambled)
print("\n\n\n\n\n\n\n")
print(unscrambled_message)

class UserInterface:
    def __init__(self):
       pass  
    def welcome():
        pass
    def quit():
        pass
    def menu():
        pass

class User_Input:
    def input_message():
        pass

class User_Output:
    def output_message():
        pass

class Security:
    def password():
        pass
    def encrypt():
        pass
    def decrypt():
        pass



def main():
    pass
