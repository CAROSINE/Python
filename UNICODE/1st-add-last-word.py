def create_new_word(word1, word2):
    # Get the first half of the first word
    half1 = word1[:len(word1)//2]
    
    # Get the second half of the second word
    half2 = word2[len(word2)//2:]
    
    # Combine them to make a new word
    new_word = half1 + half2
    return new_word

# Example usage
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

result = create_new_word(w1, w2)
print("New word:", result)
