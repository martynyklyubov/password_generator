import random
import string

def main():
    # upLetter = chr(random.randint(65,91))
    # lowLetter = chr(random.randint(97,123))
    # digit = chr(random.randint(48, 58))
    # punctSign = random.randint(33, 39)
    # password = upLetter + punctSign + digit + punctSign + digit + upLetter + lowLetter + lowLetter + upLetter + punctSign
    # password = shuffle(password)
    # print(password)

# def shuffle(string):
#     tempList = list(string)
#     random.shuffle(tempList)
#     return ''.join(tempList)

    password_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(6):
        password += random.choice(password_source)
    print(password)
    

if __name__ == '__main__':
    main()