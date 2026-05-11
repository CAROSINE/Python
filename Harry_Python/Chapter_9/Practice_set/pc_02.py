import random
 
def game():
    rand_num = random.randint(1, 100)
    user_input = None

    while user_input != rand_num:
        user_input = int(input("Guess the number between 1 and 100: "))
        if user_input < rand_num:
            print("Too low! Try again.")
        elif user_input > rand_num:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")