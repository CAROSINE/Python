with open("old.txt") as f:
    content = f.read()

with open("Rename_by_python.txt", "w") as f:
    f.write(content)