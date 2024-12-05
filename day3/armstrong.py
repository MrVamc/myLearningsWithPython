
n = input("Enter a Armstrong number:")
count = 0
for i in n:
    count = count + 1
num = int(n)
temp = num
sum = 0
while temp > 0:
    rem = temp%10
    #print(remainder)
    mul = 1
    for i in range(1,count+1):
        mul = mul * rem
    sum = sum + mul
    temp = temp// 10

if num == sum:
    print("It is an Armstrong number!!!!!")
else:
    print("It is not an Armstrong number XXXX")
