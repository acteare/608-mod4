# fig06.02.py - Amelia's Version
"""Tokenizing a string and counting unique words."""

text = ('this is similar to the example text but with more words '
        'this is more sample words that are also similar to the example text '
        'but again contain some different words '
        'here is an entirely new line that was not provided in the example text')

word_counts = {}

# count occurances of each unique word
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1 # update existing key-value pair
    else:
        word_counts[word] = 1 # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
