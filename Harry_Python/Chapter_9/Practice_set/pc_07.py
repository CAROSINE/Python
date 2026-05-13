line = 1
with open('file.txt') as f:
    line = f.readline()

    if("Donkey" in line):
        print("Donkey is present in the file")

    else:
        print("Donkey is not present in the file")