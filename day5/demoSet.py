# Example 1: Creating set
print("--- Example 1: Creating set ---")
mySet = {'A','B', 'C','D'}
print(mySet)
print("===============================")

# Example 2: Accessing the values
print("--- Example 2: Accessing the values ---")
for i in mySet:
    print(i)
print("================================")

# Example 3: Checking whether value exists or not
print("--- Example 3: Checking whether value exists or not ---")
print("B" in mySet)
print("E" in mySet)
print("================================")

# Example 4: Adding values to the set
# using add(), we can add only single value at a time
# using update(), we can add multiple values at a time
print("--- Example 4: Adding values to the set ---")
mySet.add('E')
print(mySet)
mySet.update(['F','G','H','I','J'])
print(mySet)
print("==================================")

# Example 5: Length of set
print("--- Example 5: Length of set ---")
print(len(mySet))
print("==================================")

# Example 6: Removing values in Set
# Using remove() and discard()
mySet.remove('J')
mySet.discard('I')
print(mySet)
print("==================================")

# Example 7: clearing all values from set
print("--- Example 7: clearing all values from set ---")
print(mySet)
mySet.clear() # clears all values in a set, empty set
print(mySet)
del mySet
print("===================================")

# Example 8: Joining two sets
# union(), update()
mySet1 = {1,2,3,4,5,6}
mySet2 = {'A','B','C','D'}
mySet3 = mySet1.union(mySet2)
print(mySet3)
print("===================================")

