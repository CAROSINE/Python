import re

text = "Python is fun also powerfull"

clcoding = re.findall(r"Python", text)
print(clcoding)