a = int(input("Enter his age: "))

if(a>=18):
    print("he can vote")
elif(a<0):
    print("u r kidding me")
else:
    print("he can vote after",18-a,"years")