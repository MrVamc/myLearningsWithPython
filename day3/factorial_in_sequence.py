import math
def fact(number):
    for i in range(number, 0, -1):
        print(f"{i}! = {math.factorial(i)}")

number = int(input("Enter number to find sequence of factorial : "))
print(fact(number))