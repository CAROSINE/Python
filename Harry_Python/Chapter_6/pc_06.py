post = input("Enter your post: ")

if("Mahin".lower() in post.lower()):  # here we use lower() method to convert the string into lowercase because if the user enter "mahin" instead of "Mahin" then it will also consider it as a match and print "This post is about mahin"
    print("This post is about mahin")

else:
    print("This post is not about mahin")