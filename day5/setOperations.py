friends = {"Arun", "Kiran", "Eshwar"}
foreign_friends = {"Arun", "Kiran"}
mutual_friends = friends.difference(foreign_friends)
print(mutual_friends)

mutual_friends = foreign_friends.difference(friends)
print(mutual_friends)


print("========================================================")

setone = {"one", "two"}
settwo = {"three"}
print(setone.union(settwo))


print("==========================================================")
cars = {"volve", "bmw","skoda"}
german = {"vw", "skoda", "bmw"}
print(cars.intersection(german))