from random import randint

myInput = int(input("Enter your number: "))
secretNumber = randint(1, 100)

def Hint(myInput):
    while(myInput != secretNumber):
        if myInput < secretNumber:
            print("too low")
            myInput = int(input("Enter your number: "))
        else:
            print("too high")
            myInput = int(input("Enter your number: "))

    print("correct!!")

Hint(myInput)