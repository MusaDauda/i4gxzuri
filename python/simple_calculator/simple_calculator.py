# Ask Users For Inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
while True:
    operator = input("Which operation will you like to perform? \"+\" or \"-\" or \"*\" or \"/\" or \"%\": ")
    if operator == '+':
    # Add the inputs
        result = num1 + num2
        print(f"The addition of {num1} and {num2} equals {result}")
        break
    elif operator == '-':
        #subtract the inputs
        result = num1 - num2
        print(f"The subtraction of {num1} from {num2} equals {result}")
        break
    elif operator == '*':
        # multiply the inputs
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} equals {result}")
        break

    elif operator == '/':
        # divide the inputs
        result = num1 / num2
        print(f"The division of {num1} from {num2} equals {result}")
        break

    elif operator == '%':
        #Find the modulus of inputs
        result = num1 % num2
        print(f"The modulo of {num1} by {num2} equals {result}")
        break

    else:
        print("Invalid Response")
# print(f"The addition of {num1} and {num2} equals {sum_r}")
