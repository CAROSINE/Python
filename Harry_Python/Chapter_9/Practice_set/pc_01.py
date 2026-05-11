f = open("test.txt") 
content = f.read()
if("win" in content):
    print("Yes, win is present in the file ")

else:
    print("No, win is not present in the file ")

f.close() 