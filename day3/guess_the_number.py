number = 7
while True:
    user_input = input("Would you like to play the game (Y/n): ")
    if user_input == "n":
        break

    user_number = int(input("Guess any number between 1 to 10: "))
    if user_number == number:
        print("You guessed correctly!!")
    elif abs(number - user_number) in {1,2,3,4,5,6,7,8,9}:
        print(f"You were off by {abs(number-user_number)}")
    else:
        print("Sorry! its wrong!!")
