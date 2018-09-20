def isPalindrome(str_to_test):
    start = 0
    end = len(str_to_test) - 1

    if (end <= 0):
        return True
    

    while True:
        if not (str_to_test[start] == str_to_test[end]):
            return False
        else:
            start += 1
            end -= 1
            if (start == end) or (start > end):
                return True

            


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
