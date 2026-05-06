'''
1 for snake
-1 for water
0 for gun
'''

computer = -1
youstr = input("Enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0}  # I'm  using a dictionary to convert the string input into an integer value for easier comparison
you = youDict[youstr]

if(computer == -1 and you == 0):
    print("You win")

elif(computer == -1 and you == 1):
    print("You lose")

if(computer == -1 and you == -1):
    print("You lose!")

elif(computer == 0 and you == 1):
    print("You win!")

if(computer == 0 and you == -1):
    print("You win!")

elif(computer == 0 and you == 1):
    print("You lose!")

else:
    print("something went wrong")