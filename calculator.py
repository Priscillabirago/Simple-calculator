Number = int(input("Enter first number"))
number = int(input("Enter second number"))
print(" 1: + \n 2:- \n 3:* \n 4:/ \n")
operation = int(input("What operation do you want to perform"))
if operation == 1:
    print(str(Number + number))
elif operation == 2:
    print(str(Number - number))
elif operation == 3:
    print(str(Number * number))
elif operation == 4:
    if number == 0:
        print("Division by 0 is not allowed")
    else:
        print(str(Number / number))






