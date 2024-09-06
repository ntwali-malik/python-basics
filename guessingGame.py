import random

guess = 0

num = random.randint(1, 100)    # this means it going to be from 0-100

guess = int(input("Enter a number Between 1-100: "))
while guess!=num:
    if guess==num:
        print("Congratulations Ypu Won!!")
        break
    elif guess>num:
        print("Try smaller Number")
        guess = int(input("Enter a number Between 1-100: "))
    elif guess<num:
        print("Try Bigger number")
        guess = int(input("Enter a number Between 1-100: "))
