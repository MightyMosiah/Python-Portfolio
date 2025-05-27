#Daniel Brookins
#11/21/24
#Simple Calculator
#Init
#Function
def add(num1,num2):
    result =num1 + num2
    print("The result is:"+str(result))

def sub(num1,num2):
    result = num1-num2
    print("The result is:"+str(result))
def div(num1,num2):
    result =num1/num2
    print("The result is:"+str(result))
def multi(num1,num2):
    result = num1*num2
    print( result)

def simplecalculator():
    print("Welcome Preschoolers to Simple Calculator")

    while True:

        print("Enter an operation:")
        print("""
        1.Addition
        2.Subraction
        3.Division
        4.Multiplication
        5.Quit""")
        operation= int(input("(1-5)Operation:"))
        if operation == 1:#True
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            add(int1,int2)
        elif operation == 2:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            sub(int1,int2)

        elif operation == 3:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            div(int1,int2)

        elif operation == 4:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            multi(int1,int2)

        elif operation == 5:
            break
#Main
simplecalculator()
