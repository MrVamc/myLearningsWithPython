############# Example 1 ##################
x = 10
y = 20
print(x, y)
print("===================================")
############ Example 2 ###################
x,y,z=10,20,'vamshi'
print(x,y,z)
print("===================================")
########### Example 3 ###################
x=y=z=100
print(x,y,z)
print("===================================")
########### Example 4 ##################
x,y = 10,20
print(x,y)
print('Swapping numbers')
x,y = y,x
print(x,y)

########### Example 5 ##################
name = 'vinay'
greetings = 'Good Morning'
print(f"Good morning {name}")
# f"string" is used to change the print statement dynamically.

########### Example 6 ##################
name = 'vamshi'
greet = "good afternoon, {}"
withname = greet.format(name)
print(withname)