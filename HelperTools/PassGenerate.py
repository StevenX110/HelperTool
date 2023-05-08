import string
import random

def generate_password(length=20, uppercase=True, lowercase=True, digits=True, symbols=True):
    """
    Gen random pass with your intentions
    :param length: lenght pass (по умолчанию 8 символов)
    :param uppercase: upper words (True or False)
    :param lowercase: lower words (True or False)
    :param digits: need or not it's your desicion (True or False)
    :param symbols: yeshhh (True or False)
    :return: 
    """
    if not uppercase and not lowercase and not digits and not symbols:
        raise ValueError("You have to tap Y for True at least once!")

    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Print your parametrs
print("Pass generation by Ray")
print("------------------")
length = int(input("Enter the lenght of your pass minimum 20: "))
uppercase = input("Do you want to use uppercase words? (y/n): ").lower() == "y"
lowercase = input("Do you need to use lowercase words? (y/n): ").lower() == "y"
digits = input("Do you need to use digits? (y/n): ").lower() == "y"
symbols = input("Do you need to use symbols? (y/n): ").lower() == "y"

# Gen pass
password = generate_password(length=length, uppercase=uppercase, lowercase=lowercase, digits=digits, symbols=symbols)
print("Generated password:", password)
