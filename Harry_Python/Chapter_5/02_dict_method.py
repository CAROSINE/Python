marks = {
         "mahi": 90,
         "sajol": 70,
         "olivia": 50,
         0: "Mahin"
        }

print(marks.items())
print(marks.keys()) # mahi sajol olivia , left side of dict
print(marks.values()) # 90 70 50 , right side of dict
print(marks.update({"mahi": 85 , "axl": 60})) # for update value , alos can add value or key
print(marks) # this line for update value
print(marks.get("Rock")) # for get value of key , if key is not present then it will return none
print(marks.get(0)) # for get value of key , if key is not present then it will return none

# item , keys , values , update , get these are dictionary methods
d = { } # empty dictionary
print(type(d))