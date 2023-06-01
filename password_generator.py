import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

    #Prompt the user to specify the password length 
length = int(input("Enter the desired password length: "))


    #Call the generate_password function and display the generated password
password = generate_password(length)
print("Generated Password:", password)
