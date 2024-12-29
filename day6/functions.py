# Defining a function
print("--- Example 1 : Defining a function---")
def myFunc():
    print("Hello World!!")
myFunc()
print("===========================================")

# function with arguments
print("--- Example 2 : defining function with arguments ---")
def myFuc1(name):
    print(name)
myFuc1('Earth')
print("===========================================")

# funtion with operation
print("--- Example 3 : funtion with operation ---")
def myFun2(a,b):
    print(a+b)
myFun2(2,8)
print("============================================")

# function with return statement
print("--- Example 4 : Function with return statement ---")
def myFun3(c,d):
    return (c*d)
multiple = myFun3(4,5)
print(multiple)
print("==============================================")

# function with returning nothing
print("--- Example 5 : function with returning nothing ---")
def myFun4(r):
    return
print(myFun4(3))
print("================================================")

# function without return and print statement
print("--- Example 6 : function without return and print statement ----")
def myFun5():
    i = 25
print(myFun5())
print("=================================================")