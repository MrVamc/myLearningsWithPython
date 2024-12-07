# Example 1: Creating Dictionary
print("Example 1: Creating Dictionary ")
myDictionary = {101 : 'x',
                102 : 'y',
                103 : 'z'}
print(myDictionary)
print("===============================")

# Example 2: Accessing the values from dictionary
print("Example 2: Accessing the values from dictionary")
print(myDictionary[101])
print(myDictionary.get(102))
print("===============================")

# Example 3: Editing the values in dictionary
print("Example 3: Editing the values in dictionary")
print(myDictionary)
myDictionary[103] = 'w'
print(myDictionary)
print("===============================")

# Example 4: Reading data from dictionary
print("Example 4: Reading data from dictionary")
for i in myDictionary:
    print("Prints only keys from dictionary: ",i)
for i in myDictionary:
    print("Prints only values from dictionary: ",myDictionary[i])
for i in myDictionary.values():
    print("values() is used to print the value of dictionary: ",i)
for x,y in myDictionary.items():
    print("items() is used fetch key and value pair from dictionary: ",x,y)
print("====================================")

# Example 5: Checks key exists or not in dictionary
print("Example 5: Checks key exists or not in dictionary")
if 101 in myDictionary:
    print("Present")
else:
    print("Nope")

print(109 in myDictionary)
print("====================================")

# Example 6: Length of dictionary
print("Example 6: Length of dictionary")
print(len(myDictionary))
print("================================")


# Example 7: Adding items to dictionary
print("Example 7: Adding items to dictionary")
myDictionary[104]='v'
print(myDictionary)
print("=================================")

# Example 8: copying dictionary
print(" Example 8: copying dictionary")
myDic1 = myDictionary
print(myDic1)

myDic2 = myDic1.copy()
print(myDic2)

print("=================================")

# Example 9: Removing values from dictionary
myDictionary.pop(103)
print(myDictionary)

del myDictionary[104]
print(myDictionary)

del myDictionary

myDic1.clear()
print(myDic1)

print("=====================================")




