funcs = []
for i in range(3):
    funcs.append(lambda i=i: i+i)
    for f in funcs:
        print(f())
