def reverse_mash(word1, word2):
    # Take the last half of word1 and reverse it
    half1 = word1[len(word1)//2:][::-1]
    
    # Take the first half of word2 and reverse it
    half2 = word2[:len(word2)//2][::-1]
    
    # Combine and clean up
    new_word = (half1 + half2).capitalize()
    return new_word

# Example usage
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

result = reverse_mash(w1, w2)
print("Your new word:", result)