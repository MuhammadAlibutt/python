checkAgain = True
while checkAgain:
    def checkNumber(n):
        while True:
            operand = input('Enter Number' + str(n) + ": " )
            try:
                return float(operand)
            except:
                print("Invalid Number Please enter a valid number")


    number1 = checkNumber(1)
    number2 = checkNumber(2)

    operator = input("which operation you want to perform (+, -, /, %, *): ")


    if operator == "+":
        answer = number1 + number2
    elif(operator == "-"):
        answer = number1 - number2
    elif(operator == "/"):
        if(number2 != 0 ):
            answer = number1 / number2
        else:
            print("can't divide by zero")
    elif(operator == "%"):
        if(number2 != 0):
            answer = number1 % number2
        else:
            print("can't divide by zero")
    elif(operator == "*"):
        answer = number1 * number2
    else:
        print("Invalid operator")


    print("Answer is: " + str(answer))

    askAgain = input("You want to perform an oother operation (y/n): " ).lower()

    if askAgain == "y":
        checkAgain = True
    else:
       checkAgain = False
       print("Thank you! see you Again later......")

