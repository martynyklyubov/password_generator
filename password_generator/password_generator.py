import random

def main():
    upLetter = chr(random.randint(65,90))
    lowLetter = chr(random.randint(97,122))
    digit = chr(random.randint(48, 57))
    punctSign = chr(random.randint(33, 38))

    password = upLetter + punctSign + digit + punctSign + digit + upLetter + lowLetter + lowLetter + upLetter + punctSign
    password = shuffle(password)
    print(password)


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

if __name__ == '__main__':
    main()