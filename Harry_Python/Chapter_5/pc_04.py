s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s) #20 and 20.0 are considered the same value in a set, so only one of them will be added to the set, while '20' is a different value and will be added to the set
