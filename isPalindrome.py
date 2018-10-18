#most efficient solution to problem 4


def isPalindrome(str_to_test):
    #defines the function isPalindrome
    start = 0
    #starts at 0
    end = len(str_to_test) - 1
    #end starts at end of the string
    
    if (end <= 0):
    #if the value of end is less than or equal to zero. return the value true
        return True
    

    while True:
        #continously runs the function 
        if not (str_to_test[start] == str_to_test[end]):
            #if the first and last letter do not match, return false
            return False
        else: #move one letter inward
            start += 1
            #the value of start increases by one every time the program runs
            end -= 1
            #the value of end decreases by one each time the program is run
            if (start == end) or (start > end):
            #if the value of start is equal to or greater than end, return true
                return True 

            

#test function used to check for potential bugs in the program
def testIsPalindrome():
    if (isPalindrome("1") != True):
        return False
    if (isPalindrome("12") != False):
        return False
    if (isPalindrome("abccba") != True):
        return False
    if (isPalindrome("random") != False):
        return False

    return True
