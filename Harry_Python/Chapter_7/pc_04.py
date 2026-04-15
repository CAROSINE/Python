n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number isn't prime")
        break
else:
    print("Number is prime")