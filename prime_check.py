# Check if a number is prime

num = int(input("Enter a number: "))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime")
