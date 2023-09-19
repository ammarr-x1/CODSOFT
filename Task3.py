#Task 3
# Random Password Generator


import string
import random


print("Random Password Generator")
while True:
    try:
        choice0 = int(input("\n1.Generate Password \n2.Exit\n"))
        if choice0 == 1:

            length = int(input("Enter Length of Password (minimum 8 and maximum 16) "))
            if 7 < length < 17:
                characters = ""
                print("\nChoose Complexity of Password")
                print("1.Letters Only \n2.Letters and Digits \n3.Letters,digits and punctuation")


                choice = int(input("Enter Your Choice "))
                if choice == 1:
                    characters = string.ascii_letters

                elif choice == 2:
                    characters = string.ascii_letters + string.digits

                elif choice == 3:
                    characters = string.ascii_letters + string.digits + string.punctuation

                else:
                    print("Invalid Choice")

                password = []
                for i in range(length):
                    char = random.choice(characters)

                    password.append(char)

                print("Random Password Generated " + "".join(password))

            else:
                print("Invalid character length")

        elif choice0 == 2:
            print("As you wish cutie")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input")
