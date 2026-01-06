import random

prefixes = ["ca", "zo", "re", "mi", "lo", "luu", "xi", "pa", "tri", "da"]
middles  = ["na", "li", "ra", "do", "mo", "que", "ze", "ki", "sha"]
suffixes = ["on", "ix", "ar", "en", "us", "eth", "or", "um", "iel"]

def generate_word():
    word = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return word.capitalize()

for _ in range(5):
    print(generate_word())
