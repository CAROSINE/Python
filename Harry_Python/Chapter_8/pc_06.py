def inch_cms(inch):
    return inch * 2.54

n = int(input("Enter a number in inches: "))
print(f"The corresponding valure in cms is: {inch_cms(n)}")