# input() function takes input from the user, it considers inputs in string format only.
q=input("Enter any number :")
print(type(q))
print("==================================")
# converting string into int by using int(), Approach 1
w = int(input("Enter any number 1: "))
e = int(input("Enter any number 2: "))
print(w+e)
print("===================================")
#approach 2
r = input("Enter num1: ")
t = input("Enter num2: ")
print(int(r)+int(t))
print("===================================")
# converting string into float by using float(), approach 1
y = float(input("provide decimal no1: "))
u = float(input("provide decimal no2: "))
print(y+u)
print("===================================")
#approach 2
i = input("enter decimal no1: ")
o = input("enter decimal no2: ")
print(float(i)+float(o))
