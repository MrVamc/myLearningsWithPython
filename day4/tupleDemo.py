# Example 1:  Creating a Tuple
print("--- Example 1:  Creating a Tuple ---")
mytuple = ("Volve","BMW","Mercedes")
print(mytuple)

myemptyTuple = ()
print(myemptyTuple)

print("========================================")

# Example 2: Accessing Tuple values
print("--- Example 2: Accessing Tuple values ---")
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])

print("==========================================")

# Example 3: Range of indexes
print("--- Example 3: Range of indexes ---")
print(mytuple[0:3])
print(mytuple[-3:-1])

print("===========================================")

# Example 4: Changing the values of Tuple
# Tuples are Immutable
# -> We cannot modify existing values
# -> We cannot append new values
# -> We cannot insert a new value
# -> We cannot remove a value
# But we can do it in alternate way
# By converting tuple to list -> modify list -> list to tuple

print("--- Example 4: Changing the values of Tuple ---")
print("converting tuple to list -> modify list -> list to tuple")
mytuple = list(mytuple)
print("Tuple converted into : ",type(mytuple))
mytuple.append("Ferrari")
mytuple.append("Range Rover")
print("Updated List : ",mytuple)
mytuple = tuple(mytuple)
print("List converted into : ", type(mytuple))

print("=========================================================")

# Example 5: Fetching tuple using loop
print("--- Example 5: Fetching tuple using loop ---")
for i in mytuple:
    print(i)

print("==========================================================")

# Example 6: Value exists in tuple or not
print("--- Example 6: Value exists in tuple or not ---")
if 'Ferrari' in mytuple:
    print("Yes, it is in tuple")
else:
    print("no, it is not in tuple")

print("==========================================================")

# Example 7: Finding Tuple length
print("--- Example 7: Finding Tuple length ---")
print(len(mytuple))

print("==========================================================")

# Example 8: Copying tuple
print(mytuple)
myNewTuple = mytuple
print(myNewTuple)

print("=========================================================")

# Example 9: Joining / Combining tuple
print("--- Example 9: Joining / Combining tuple ---")
myNewTuple2 = mytuple + myNewTuple
print(myNewTuple2)

print("==========================================================")