print("Example : 1")
def func(i,j):
    print(i,j)
func(10,20) # positional argument
func(i = 20, j = 35) # Keyword argument

print("=================================")

print("Example : 2")
def func1(i, j=35):
    print(i,j)
func1(100,200)
func1(100)
print("==================================")

print("Example : 3 ")
def func2(name, greetings):
    print(greetings+" "+ name)
func2(name = 'vamshi', greetings= 'hello') # key arguments
func2(greetings='good morning', name='vamshi')
print("=======================================")

print("Example : 4")
def func3(a,b,c):
    print(a,b,c)
func3(10,20,30) # positional arguments
func3(a = 20, b = 30 , c = 40) # key arguments
func3(c= 50, a=60, b=70) # key arguments
print("Positional argument must appear before any key argument")
func3(10,70,c=70)
print("===========================================")

print("Example : 5")
def func4(a,b):
    if a > b:
        return a,b
    else:
        return b,a
result = func4(20,45)
print(result)
print(type(result))
print("=============================================")

