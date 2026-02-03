games = [ "ff", "pubg", "gta", "nfs" ]  # ekta list create korlam jekhane kichu game name store kora ache
                                        # [] list er jonno use kora hoi
g1 = input("Enter game name: ")   # append er kaj holo list er seshe notun element add kora
games.append(g1)

g2 = input("Enter game name: ") # input diye user theke game name nibo
games.append(g2)

g3 = input("Enter game name: ")
games.append(g3)

print(games)
print(len(games)) # len() function ta list er length ba size return kore