import random
import string

def generate_password(length):
    # Define the character sets to generate the password from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        
        if length <= 0:
            print(" for generate a password the Length should be greater than zero.")
        else:
            password = generate_password(length)
            print("Your  automated generated password is:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
