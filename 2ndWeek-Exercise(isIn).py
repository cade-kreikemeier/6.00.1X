def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) <= 1 and char != aStr:
        return False

    if char == aStr[len(aStr)//2]:
        return True

    if char < aStr[len(aStr)//2]:
        aStr = aStr[:len(aStr)//2]
    else:
        aStr = aStr[len(aStr)//2:]
    return isIn(char, aStr)


print(isIn('b', 'abcdefg'))