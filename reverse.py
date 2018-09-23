#Manav Shardha
#IC4U0
#September 21st,2018
#The function of this program is to test a string to see if it is an palindrome

import time
#imports the python library time

def welcome():
#defines the functions welcome, used to inform the user of this program and to improve the user experience
    print(
    "-------------------------------------------------------------- \n",
    "           Welcome to the Palindrome Conundrum                \n" +
    "--------------------------------------------------------------\n"+
    "The function of this program is to test a given input \n to see if it is a palindrome")
    #prints welcome message

def str_input():
    #defines the function str_input, it is used to get the 
    global user_input
    user_input = input("Please enter a string you wish to check: \n >>> ")

def exit_message():
    print("Thank you for using the World of Triangles")
    time.sleep(.5)
    print("exiting...")
    time.sleep(0.3)
    exit()


def quit_intent():
    user_intent = input("Do you wish to use this program again? \n Type Yes or No \n Selection: ").lower()
    while not((user_intent == 'yes') or (user_intent == 'no')):
        user_intent = input("The input you have entered is considered invalid, Please re-enter your selection\n"+
                            "Do you wish to use this program again again? \n Type Yes or No \n Selection: ").lower()
    if user_intent == 'yes':
        pass
    elif user_intent == 'no':
        exit_message()
    else:
        pass


def test_palindrome():
    r_user_input = ''.join(reversed(user_input))
    if r_user_input == user_input:
        print("The input you have entered is a palindrome\n\n")
    else:
        print("The input you have entered is not a palindrome\n\n")
    
def main():
    while True:
        welcome()
        str_input()
        test_palindrome()
        quit_intent()
    
main()
