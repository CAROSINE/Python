a = int(input("Enter his age: "))

if(a%2 == 0):     # if statement 1
    print("a is even")
                            # both if statement are independent
# end of if statement 1                          
if(a>=18):        # if statement 2
    print("he can vote")  # before print , the spacxe is called indentation and it is used to define the block of code which is to be executed when the condition is true

elif(a<0):
    print("u r kidding me")

else:
    print("he can vote after",18-a,"years")
# end of if statement 2