"""
Word Occurrences
Estimate: 50 minutes
Actual:  70  minutes
"""

word_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.keys())

max_length = max(len(word) for word in sorted_words)

for sorted_word in sorted_words:
    print(f"{sorted_word:{max_length}} : {word_count[sorted_word]}")

# I was struggling with this one and kept going back and forth so I am not sure if I did it wrong but the output matches
