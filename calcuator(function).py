def addition(Number, number):
    return Number + number


def subtraction(Number, number):
    return Number - number


def product(Number, number):
    return Number * number


def division(Number, number):
    if number == 0:
        return "Division by 0 is not allowed"
    else:
        return Number / number


Number = int(input("Enter first number"))
number = int(input("Enter second number"))
print(" 1: + \n 2:- \n 3:* \n 4:/ \n")
operation = int(input("What operation do you want to perform"))
if operation == 1:
    print(addition(Number, number))
elif operation == 2:
    print(subtraction(Number, number))
elif operation == 3:
    print(product(Number, number))
elif operation == 4:
    print(division(Number, number))








