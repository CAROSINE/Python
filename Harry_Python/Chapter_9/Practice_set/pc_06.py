word = ["Donkey", "Monkey", "Turkey"]

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content
for w in word:
    contentNew = contentNew.replace(w, "######")

with open("file.txt", "w") as f:
    f.write(contentNew)