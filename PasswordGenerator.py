import random


def password_generator(level, length):
    password = ""
    level1 = "abcdefghijklmnopqrstuvwxyz"
    level2 = "0123456789"
    level3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    level4 = "`~!@#$%^&*()-_=+[]{};:\'\"\\,<.>/?"

    # This part guarantees each of the criteria
    if level >= 1:
        password += level1[random.randint(0, len(level1) - 1)]
    if level >= 2:
        password += level2[random.randint(0, len(level2) - 1)]
    if level >= 3:
        password += level3[random.randint(0, len(level3) - 1)]
    if level == 4:
        password += level4[random.randint(0, len(level4) - 1)]

    # This will randomize each remaining character of the password. For loop starts from index after
    # the criteria has been fulfilled. Will not run if level = length
    for i in range(level, length):
        randomizer = random.randint(1, level)
        if randomizer == 1:
            password += level1[random.randint(0, len(level1) - 1)]
        elif randomizer == 2:
            password += level2[random.randint(0, len(level2) - 1)]
        elif randomizer == 3:
            password += level3[random.randint(0, len(level3) - 1)]
        else:
            password += level4[random.randint(0, len(level4) - 1)]

    # This will randomize the string by popping values out of a set to recreate the string.
    # This is needed because the 1st value will always be lowercase, 2nd is number, 3rd is uppercase, and 4th is symbol
    password = set(password)
    final_password = ""
    for i in range(len(password)):
        final_password += password.pop()
    print(final_password)


n = 0
while n != 1 and n != 2 and n != 3 and n != 4:
    n = int(input("On a scale of 1 - 4, how strong do you want your password to be?\n\
    1 - Lowercase letters\n\
    2 - lowercase letters and numbers\n\
    3 - lowercase letters, numbers, and uppercase letters\n\
    4 - lowercase letters, numbers, uppercase letters, and symbols\n\
    Enter here: "))

m = input("How many characters do you want it to be? Enter a number: ")
# This will not error out because if m is not a digit, the while loop will not evaluate the 2nd criteria
while not m.isdigit() or int(m) < n:
    m = input("It must be a number and the length must exceed the level to fit all types of characters: ")

password_generator(n, int(m))
