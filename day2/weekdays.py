week = int(input("Enter week number : "))
if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
elif week<=0:
    print("provide valid week day")
else:
    print("We have only 7 days in a week")