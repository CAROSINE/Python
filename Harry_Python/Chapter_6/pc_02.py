marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

# check for total percentage
total_percentage = (marks1 + marks2 + marks3)/300 * 100

if(total_percentage>=40 and marks1>=40 and marks2>=40 and marks3>=40):
    print("Student has passed.")
else:
    print("Student has failed.")