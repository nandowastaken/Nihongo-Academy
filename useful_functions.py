# returns -1 if negative, 1 if positive or 0 if the number is 0
def operatorSign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def mastery_classification(points):
    if points % 5 == 0:
        return True
    else:
        return False

def translateAlphabet(letter, alphabet):
    return alphabet[letter]
