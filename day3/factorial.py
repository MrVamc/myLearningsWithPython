mul = 1
num = int(input("enter factorial of : "))
for i in range(1,num+1):
    mul = i * mul
    i = i + 1
print("Factorial of ",num," : ",mul)