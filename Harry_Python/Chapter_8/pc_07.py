def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["mahin" , "robin" , "harry" , "ron" , "hermione"]
print(rem(l, "ron"))