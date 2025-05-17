myList = [1,2,3,4]
mylist2 = [num * 2 for num in myList]
print(mylist2)
print("=================================")

myfriends = ['Vamshi', 'Varun', 'Ajay', 'Teja']
myfriend2 = [friend for friend in myfriends if friend.startswith("V")]
print(myfriend2)