print("Example 1")
var1 = 10 # global variable
def fun():
    var2 = 20 # local variable
    print("printing local variable : ",var2)
    print("printing global variable : ", var1)
print(fun())
print("printing global varibale : ",var1)
print("We cannot print local variable outside the function.")
print("=====================================================")

print("Example 2")
xy = 100 # global variable
def fun1():
    xy = 200 # local variable
    print(xy)
fun1() # it prints local variable only
print("=======================================================")

print("Example 3")
v = 100
def fun2():
    global v # accessing global variable wit 'global' keyword
    v = 150 # changing the value of global variable
    print(v)
fun2()
print(v) # prints changes value only
print("=======================================================")

print("Example 4")
def fun3():
    global x
    x = 130
    print(x)
print(x) #will get error
print("=========================================================")