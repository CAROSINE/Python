def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["mahin" , "robin" , "harry" , "ron" , "hermione"]
print(rem(l, "n"))