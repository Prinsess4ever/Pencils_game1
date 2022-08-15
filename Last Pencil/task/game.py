import random


def cometaar_on_the_plencils(value):
    aantal = 0
    while True:
        if aantal != 0:
            value = input("How many pencils would you like to use:\n")
        if not value.isnumeric():
            print("The number of pencils should be numeric")
            aantal += 1
        elif value == "0":
            print("The number of pencils should be positive")
            aantal += 1
        else:
            break
    return value

def commentaar_on_names(name):
    aantal = 0
    list_of_names = ["John", "Jack"]
    while True:
        if aantal != 0:
            name = input("Who will be the first (John, Jack):\n")

        if name not in list_of_names:
            print("Choose between 'John' and 'Jack'")
            aantal += 1
        else:
            break
    return name

def ask_pencils(who):
    while True:
        number = input(who + "'s turn:\n")

        if not number.isnumeric():
            print("Possible values: '1', '2' or '3'")
        elif number != "1" and number != "2" and number != "3":
            print("Possible values: '1', '2' or '3'")
        else:
            return int(number)

aantal = 0
how_many_pencils = input("How many pencils would you like to use:\n")
how_many_pencils = cometaar_on_the_plencils(how_many_pencils)
name_who_first = input("Who will be the first (John, Jack):\n")
name_who_first = commentaar_on_names(name_who_first)
print("|"*int(how_many_pencils))
bot = "Jack"

def other_player_brain(pencils_left):
    value = (int(pencils_left) - 1) % 4 + 1

    if value == 1:
        return 1
    elif value == 2:
        return 1
    elif value == 3:
        return 2
    else:  # value == 4:
        return 3


while True:
    if bot == "Jack" and name_who_first == "Jack":
        print("Jack's turn")
        how_many = other_player_brain(how_many_pencils)
        print(how_many)
    elif bot == "John" and name_who_first == "John":
        print("John's turn")
        how_many = other_player_brain(how_many_pencils)
        print(how_many)
    else:
        how_many = ask_pencils(name_who_first)

    if (int(how_many_pencils) - int(how_many)) < 0:
        print("Too many pencils were taken")
        if name_who_first == "John":
            name_who_first = "Jack"
        else:
            name_who_first = "John"
    else:
        how_many_pencils = int(how_many_pencils) - int(how_many)
        if how_many_pencils != 0:
            print("|"*how_many_pencils)

    if (int(how_many_pencils) - int(how_many)) <= 0:
        name_who_first = name_who_first
    if name_who_first == "John":
        name_who_first = "Jack"
    else:
        name_who_first = "John"

    if how_many_pencils == 0:
        break

print(name_who_first + " won!")