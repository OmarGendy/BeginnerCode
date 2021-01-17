import datetime


def age_check():
    """
    Takes a user's name and age and prints the year they will turn 100
    :return: true/false
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    while(age.isdigit() == False):
        age = input("Enter a number idiot: ")
    age = int(age)
    if age >= 100:
        print("You're already old")
        return True
    remainder = 100 - age
    year = datetime.datetime.now().year
    print(name + ", you will be 100 years old by the year " + str(year+remainder) + ".")
    True


age_check()