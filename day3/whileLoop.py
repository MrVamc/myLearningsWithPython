# example 1
# print numbers from 1 to 10
i=1 #initialization
while i<=10: #condition
    print(i)
    i=i+1   #increment
print("1 to 10 numbers have printed")
print("==============================")

# example 2
#print numbers in descending order
j = 10
while j>=0:
    print(j)
    j=j-1
print("Descending order have printed")



def count_digits(number):
    count = 0
    while number:
        count += 1
        number //= 10  # Integer division by 10
    return count

# Example usage
print(count_digits(12345))  # Output: 5
