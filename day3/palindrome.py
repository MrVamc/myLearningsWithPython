n = input("Enter a string: ")
reverse = ""
for i in n:
    reverse = i + reverse
if n == reverse:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")