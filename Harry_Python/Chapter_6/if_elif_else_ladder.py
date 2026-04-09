a = int(input("Enter his age: "))

if(a>=18):
    print("he can vote")  # before print , the spacxe is called indentation and it is used to define the block of code which is to be executed when the condition is true

elif(a<0):
    print("u r kidding me")

elif(a<18):
    print("you're entering invalid age")

else:
    print("he can vote after",18-a,"years")