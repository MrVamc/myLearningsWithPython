# Example 1: How to create list
print("--- Example 1 : How to create list ----")
mylist1 = [10,20,30,40]
print(mylist1)

mylist2 = ["apple","banana","cherry"]
print(mylist2)

mylist3 = ["apple",10,"banana",20]
print(mylist3)

mylist = list() #empty list
print(mylist)

print("===============================")

# Example 2: Accessing items from the list
print("--- Example 2 : Accessing items from the list ----")
demoList = ['Apple','Banana','Mango'] # fetches values through indexing, starts from 0.
print(demoList[0])
print(demoList[1])
print(demoList[2])
print("With negative values -1 : ",demoList[-1])
print("With negative value -2 : ", demoList[-2])
print("With negative value -3 : ", demoList[-3])

print("===============================")

# Example 3: Range of indexes
print("--- Example 3 : Range of indexes ----")
demoList1 = ['Volvo','BMW','Mercedes','Suzuki','Audi','Nissan','Mini Cooper','Jaguar','Range Rover']
print(demoList1[2:5])
print(demoList1[-4:-1])

print("==============================")

# Example 4: Changing or updating the values
print("--- Example 4 : Changing or updating the values ----")
print(demoList1[3])
demoList1[3] = 'Ferrari'
print(demoList1[3])
print(demoList1)

print("===============================")
# Example 5: fetching values using for loop
print("--- Example 5 : fetching values using for loop ----")
print(demoList1)
for i in demoList1:
    print(i)
print("=================================")

# Example 6: check is value is present in the list
print("--- Example 6 : check is value is present in the list ---")
print(demoList1)
if 'Ferrari' in demoList1:
    print("Yes, Ferrari is in the list.")
else:
    print("No, Ferrari is not in the list.")

print("====================================")

# Example 7: Finding length of a List
print("--- Example 7 : Finding length of a List ---")
print(demoList1)
print(len(demoList1))
print("======================================")

# Example 8: Adding new elements into the list
print("--- Example 8 : Adding new elements into the list ---")
print(demoList1)

demoList1.append("Honda") # append() inserts elements at the end of the list
print(demoList1)

demoList1.insert(4,'Mclaren') # insert() is used to insert elements in between the list by providing the indexes.
print(demoList1)

print("========================================")
# Example 9: Removing the elements using pop(), clear()  and del
print("--- Example 9 : Removing the elements using pop(), clear()  and del ---")
print(demoList1)

print(demoList1.pop(0)) #pop() function removes an element from the list
print(demoList1)

del demoList1[-1] #del is keyword used to remove an element from the list\
print(demoList1)

#demoList1.clear() clear() function clear all the elements in the list and prints empty list
#print(demoList1)
print("=========================================")

# Example 10: Copying list using list(), copy(), for loop and extend()
print("--- Example 10 : Copying list ---")
print(demoList1)

cars = list(demoList1)
print(cars)

fourWheelers = demoList1.copy()
print(fourWheelers)

# Example 11: combining the two lists.
seq = ['a','b','c']
seq1 = [1,2,3]
seq2 = seq + seq1
print(seq2)

seq3 = ['A','B','C']
for i in seq3:
    seq.append(i)
print(seq)

seq4 = [4,5,6]
seq2.extend(seq)
print(seq2)
