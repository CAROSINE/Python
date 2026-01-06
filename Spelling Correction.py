from textblob import TextBlop

blop = TextBlop("Juss dee oit")
corrected_blop = blop.correct()

print("Original Text:", blop)
print("Corrected Text:", corrected_blop)