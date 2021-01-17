num1 = ""
while type(num1) == str:
    try:
        num1 = input('Enter first number: ')
        num1 = float(num1)
    except ValueError:
        print("That's not a number idiot, try again")

num2 = ""
while type(num2) == str:
    try:
        num2 = input('Enter second number: ')
        num2 = float(num2)
    except ValueError:
        print("That's not a number idiot")

print(num1 + num2)
