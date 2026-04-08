s1={1,2} # if 7,8 are added to s1, then it will not be a subset of s2 , falls the condition of subset and superset
s2={1,2,3,4,5}

print(s1.issubset(s2) or s1 <= s2) # for subset
print(s2.issuperset(s1) or s2 >= s1) # for superset