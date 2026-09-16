import random

def guess():
    print("I am picking a number between 0 - 100")
    print("Play with me")
    attempt = 0
    while True:
        n = int(input("Enter a number: "))
        num = random.randint(0, 100)
        attempt += 1
        if n < 0 or n > 100:
            print("invalid number")
        elif n != num:
            print("Try Again")
        else:
            print("you guessed the number")
            break
        if attempt > 3:
            print("Time out, Try again later")
            break

guess()

print("Calculate into your future")
def calc():
    n1 = int(input("Enter a number: "))
    operator = input("Enter an Operator, +-/*: ")
    n2 = int(input("Enter another number: "))
    if operator == "+":
        print("Total = ",n1 + n2)
    elif operator == "-":
        print("Total = ", n1 - n2)
    elif operator == "*":
        print("Total = ", n1*n2)
    elif operator == "/":
        print("Total = ", n1/n2)
    else:
        print("Invalid operator")
calc()

print("Multiplication table from 1-13")
def multiplication():
    n = int(input("Enter a number: "))
    for x in range(1,13):
        result = n*x
        print(f"{n} * {x} = {result}")

multiplication()

print("Lambda usage practice")
names = ["fatiah", "bushra", "dave"]
average = lambda x: sum(x)/len(x)
print(average([3,6,9]))

cap = map(lambda x: x.upper(), names)
print(list(cap))