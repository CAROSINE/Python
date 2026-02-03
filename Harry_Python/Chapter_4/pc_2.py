marks = [ ]  # ekta list create korlam jekhane kichu marks here  store kora ache
                                        # [] list er jonno use kora hoi
m1 = int(input("Enter marks here : "))   # append er kaj holo list er seshe notun element add kora
marks.append(m1)

m2 = int(input("Enter marks here : ")) # int(input diye user theke marks here)  nibo
marks.append(m2)

m3 = int(input("Enter marks here : "))
marks.append(m3)

m4 = int(input("Enter marks here : "))
marks.append(m4)

m5 = int(input("Enter marks here : "))
marks.append(m5)  

m6   = int(input("Enter marks here : "))
marks.append(m6)

marks.sort() # sort() function ta list er element gulo ke ascending order e sort kore
print(marks)
print(len(marks)) # len() function ta list er length ba size return kore