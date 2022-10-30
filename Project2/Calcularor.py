
# Defining fuction
def calculate():
    print("Welcome to the calculator program: ")
    op = input("""
please enter the math operation you would like to perform:
+ for addition
- for subtration
* for multiplication
/ for division
""")

# Conditional Statements

    if op == "+":
        numb1 = int(input("Enter your first number: "))
        numb2 = int(input("Enter your second number: "))
        print(" {} + {} = ".format(numb1, numb2))
        print(numb1 + numb2)

    elif op == "-":
        numb1 = int(input("Enter your first number: "))
        numb2 = int(input("Enter your second number: "))
        print(" {} - {} = ".format(numb1, numb2))
        print(numb1 - numb2)

    elif op == "*":
        numb1 = int(input("Enter your first number: "))
        numb2 = int(input("Enter your second number: "))
        print(" {} * {} = ".format(numb1, numb2))
        print(numb1 * numb2)

    elif op == "/":
        numb1 = int(input("Enter your first number: "))
        numb2 = int(input("Enter your second number: "))
        print(" {} / {} = ".format(numb1, numb2))
        print(numb1 / numb2)
    
    else:
        print("invalid input, please run the program again.")
        
# Define again() function to allow the user to perform the calculation again
    again()
 
def again():
    cal_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO.
""")

    if cal_again.upper() == "Y":
        calculate()
    elif cal_again.upper() == "N":
        print("Thank for using the calculator program: see you next time!!")
    else:
        again()

calculate()

    





