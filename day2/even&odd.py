# Approach 1
number = int(input("Enter a number: "))
if number%2 == 0:
    print("Given number %d is : Even number!!" %(number))
else:
    print("Given number %d is : Odd number!!" %(number))
print("================================================")
# Approach 2 Ternary operator
num = int(input("Enter number : "))
print("Even") if num%2==0 else print("odd")
print("==================================================")
# Approach 3 printing multiple statements in single statement
num = 20
{print("even"), print("Number")} if num%2 ==0 else {print("odd"), print("Number")}