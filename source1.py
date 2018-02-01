import random

keep_going = True


def random_number():
    num = random.randint(1, 6)
    print(num)
    return


while keep_going:
    x = input("Would you like to continue the game?\n")

    if x.lower() == "yes":
        random_number()

    if x.lower() == "no":
        print("The game has now ended")
        keep_going = False
