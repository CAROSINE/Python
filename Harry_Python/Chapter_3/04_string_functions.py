name = "carosine"
print(len(name)) # output 8

print(name.endswith("ine"))
print(name.startswith("caro"))

print(name.capitalize())

S = "I'm carosine"
replaced_S= S.replace("carosine", "Moshiur Rahman Sajol")
print(replaced_S) # output I'm Bitrox

print(name.find("ros"))
print(name.count("o")) # output 1

print(name.isalnum())   # output True, as it contains only letters
print(name.isalpha())   # output True, as it contains only letters
print(name.isdigit())   # output False, as it contains letters
print(name.islower())
print(name.isupper())   # output False, as it contains lowercase letters
print(name.upper())    # output CAROSINE
print(name.lower())    # output carosine

print(name.title())    # output Carosine
print(name.swapcase()) # output CAROSINE