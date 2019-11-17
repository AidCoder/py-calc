#This is a simple calculator program write in Python based on 'user-inputs'


#Add two numbers
def add(number1, number2):
    return number1 + number2


#Substract two numbers
def substract(number1, number2):
    return number1 - number2


#Multiply two numbers
def multiply(number1, number2):
    return number1 * number2


#Divide two numbers
def divide(number1, number2):
    return number1 / number2


#This is the 'user-inputs' part
print("Enter your name")
user_name = input("")

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    #If the user's input is 'quit', the program will shut down!
    if user_input == 'quit':
        break
    #We use the add function
    elif user_input == 'add':
        number1 = int(input("Enter first number \n"))
        number2 = int(input("Enter second number \n"))
        print("The result is \n" + number1 + " + ", number2,
              " = " + add(number1, number2))
    #We use the substract function
    elif user_input == 'substract':
        number1 = int(input("Enter first number \n"))
        number2 = int(input("Enter second number \n"))
        print("The result is \n" + number1, " - " + number2,
              " = " + substract(number1, number2))
    #We use the multiply function
    elif user_input == 'multiply':
        number1 = int(input("Enter first number \n"))
        number2 = int(input("Enter second number \n"))
        print("The result is \n" + number1 + " * " + number2 + " = " +
              multiply(number1, number2))
    #We use the divide function
    elif user_input == 'divide':
        number1 = int(input("Enter first number \n"))
        number2 = int(input("Enter second number \n"))
        print("The result is \n" + number1 + " / " + number2,
              " = " + divide(number1, number2))
    else:
        print("Cannot run, please try again!")
print("Thank you for playing " + user_name)