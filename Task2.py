# Task 2
#simple calculator

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def main():
    print("\n\t\tSimple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")



    while True:
        try:
            choice = int(input("\n**** CHOOSE AN OPERATION (1/2/3/4/5) ****"))
            if choice == 1:
                num1 = float(input("First Number :"))
                num2 = float(input("Second Number : "))

                print(f"{num1} + {num2} = ",add(num1,num2))


            elif choice == 2:
                num1 = float(input("First Number :"))
                num2 = float(input("Second Number : "))

                print(f"{num1} - {num2} = ", subtract(num1, num2))

            elif choice == 3:
                num1 = float(input("First Number :"))
                num2 = float(input("Second Number : "))

                print(f"{num1} * {num2} = ", multiply(num1, num2))

            elif choice == 4:
                 num1 = float(input("First Number :"))
                 num2 = float(input("Second Number : "))

                 print(f"{num1} / {num2} = ", divide(num1, num2))

            elif choice == 5:
                break

            else:
                print("Invalid Choice")
        except:
            print("Invalid")

main()