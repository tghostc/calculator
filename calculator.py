from os import system
from sys import exit

def printHelp():
    print("Welcome to the calculator. Type \"add\" for addition, \"subtract\" for subtraction, \"multiply\" for \nmultiplication, and \"divide\" for division. Type \"clear\" to clear the screen, to quit type \"quit\",\nor to display this help type \"help\".")

def clearScreen():
    system("cls")

def getOption():
    return input("\n> ")

def add():
    while True:
        try:
            x = float(input("Enter a number to add. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to add.")
            print("")

    while True:
        try:
            y = float(input("Enter a number to add " + str(x) + " by. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to add " + str(x) + " by.")
            print("")

    addAns = x + y
    add.result = str(x) + " + " + str(y) + " = " + str(addAns)
    return add.result

def subtract():
    while True:
        try:
            x = float(input("Enter a number to subtract. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to subtract.")
            print("")

    while True:
        try:
            y = float(input("Enter a number to subtract " + str(x) + " by. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to subtract " + str(x) + " by.")
            print("")

    subtractAns = x - y
    subtract.result = str(x) + " - " + str(y) + " = " + str(subtractAns)
    return subtract.result

def multiply():
    while True:
        try:
            x = float(input("Enter a number to multiply. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to multiply.")
            print("")

    while True:
        try:
            y = float(input("Enter a number to multiply " + str(x) + " by. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to multiply " + str(x) + " by.")
            print("")

    multiplyAns = x * y
    multiply.result = str(x) + " * " + str(y) + " = " + str(multiplyAns)
    return multiply.result

def divide():

    while True:
        try:
            x = float(input("Enter a number to divide. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to divide.")
            print("")

    while True:
        try:
            y = float(input("Enter a number to divide " + str(x) + " by. "))
            break

        except ValueError:
            print("Error! Please try again, enter a number to divide " + str(x) + " by.")
            print("")

    divideAns = x / y
    divide.result = str(x) + " / " + str(y) + " = " + str(divideAns)
    return divide.result

clearScreen()
printHelp()

while True:
    getOpt = getOption()

    if getOpt.lower() == "add":
        clearScreen()
        add()
        print("")
        print(add.result)

    elif getOpt.lower() == "subtract":
        clearScreen()
        subtract()
        print(subtract.result)

    elif getOpt.lower() == "multiply":
        multiply()
        clearScreen()
        print(multiply.result)

    elif getOpt.lower() == "divide":
        clearScreen()
        divide()
        print(divide.result)

    elif getOpt.lower() == "clear":
        clearScreen()

    elif getOpt.lower() == "help":
        clearScreen()
        printHelp()

    elif getOpt.lower() == "quit":
        exit(0)

    else:
        print("")
        print("That is invalid input, please try again.")
