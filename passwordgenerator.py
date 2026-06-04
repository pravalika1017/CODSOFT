import random
import string

print("Password Generator")

while True:

    # Password length
    length = int(input("Enter Password Length: "))

    # Complexity options
    print("\nSelect Password Type")
    print("1. Numbers Only")
    print("2. Letters Only")
    print("3. Letters and Numbers")
    print("4. Letters, Numbers and Symbols")

    choice = input("Enter Choice (1-4): ")

    # Character selection
    if choice == '1':
        characters = string.digits

    elif choice == '2':
        characters = string.ascii_letters

    elif choice == '3':
        characters = string.ascii_letters + string.digits

    elif choice == '4':
        characters = string.ascii_letters + string.digits + string.punctuation

    else:
        print("Invalid Choice")
        continue

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # Display password
    print("\nGenerated Password:", password)

    # Continue option
    again = input("\nGenerate Another Password? (yes/no): ")

    if again.lower() != 'yes':
        print("Program Closed")
        break