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
    #declares the variable user_input as a global variable
    #thus allowing it to be used in other functions 
    user_input = input("Please enter a string you wish to check: \n >>> ")
    #asks the user to enter an input and stores it in the variable user_input
    
def exit_message():
    #defines the function exit_message, used to improve the user interface
    print("Thank you for using the Palindrome Conundrum")
    #prints message for the user
    time.sleep(.5)
    #the program pauses for 0.5 seconds and then resumes
    print("exiting...")
    #prints message for the user
    time.sleep(0.3)
    #the program pauses for 0.3 seconds and then resumes
    exit()
    #exits the program 


def quit_intent():
    #defines the function quit_intent(), used to allow the user to exit the program
    user_intent = input("Do you wish to use this program again? \n Type Yes or No \n Selection: ").lower()
    #user's desire to continue or end the program is stored in the variable user_intent
    #.lower() makes the entire string lower case, used to account for case errors
    while not((user_intent == 'yes') or (user_intent == 'no')):
        #continously running loop that will only stop if the user input is either yes or no 
        user_intent = input("The input you have entered is considered invalid, Please re-enter your selection\n"+
                            "Do you wish to use this program again again? \n Type Yes or No \n Selection: ").lower()
        #informs the user that they entered an incorrect input and asks the user to re-enter the input
    if user_intent == 'yes':
        pass
        #do nothing
    elif user_intent == 'no':
        exit_message()
        #calls the function exit_message
    else:
        pass
        #do nothing


def test_palindrome():
    #defines the function test_palindrome()
    r_user_input = ''.join(reversed(user_input))
    #the reversed function analyzes the characters in the string, rearranges them in reverse order.
    #the ''.join function joins the characters with no spaces in between back into a string
    if r_user_input == user_input:
        #conditional statement, where if the reverse of the user_input is the same as user_input,
        #execute subcommand
        print("The input you have entered is a palindrome\n\n")
        #informs the user that the string that they entered is a palindrome
    else:
        #if r_user_input does not equal user_input, execute subfunctions
        print("The input you have entered is not a palindrome\n\n")
        #informs the user that the string that they entered is not a palindrome
    
def main():
    #defines the function main, used to consolidate the code
    while True:
        #keeps the program running continously
        welcome()
        #calls the function welcome()
        str_input()
        #calls the function str_input()
        test_palindrome()
        #calls functions test_palindrome()
        quit_intent()
        #calls the functions quit_intent()
    
main()
#executes the problems
