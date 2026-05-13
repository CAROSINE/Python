
with open('file.txt') as f:
    line = f.readline()

lineno = 1
for line in f:
    lineno += 1
    if("Donkey" in line):
        print(f"Donkey is present in the file at line {lineno}")

    else:
        print("Donkey is not present in the file")