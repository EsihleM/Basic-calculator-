import math
def calculator():
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    operator = input("choose an operator: * - / + ")

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "/":
        if num2 !=0:
            answer = num1/num2
        else:
            return "cannot divide by zero"
    elif operator == "*":
        answer = num1*num2
    else:
        return "enter a valid operator"
    print(f"{num1} {operator} {num2} = {answer}")
    
calculator()
