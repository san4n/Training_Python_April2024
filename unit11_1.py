#---------

d = {'A': 100, 'B': 200}

print(d['A'])

# Define dictionary
d = {
    'dog': 'has a tail and barks',
    'cat': 'says meow',
    'bird': 'can fly',
    'fish': 'swims in water'
}

# Ask user for a word
word = input("Enter a word to look up: ").lower()

# Lookup
if word in d:
    print(f"{word}: {d[word]}")
else:
    print("Word not found in dictionary.")

#---------


# Define points for each letter (Scrabble-style)
points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2,
    'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10,'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

# Ask user for a word
word = input("Enter a word: ").upper()

# Calculate score
score = sum([points[c] for c in word if c in points])

print("Score for", word, "is:", score)

#-----------

# Define suits
suits = ['hearts', 'diamonds', 'clubs', 'spades']

# Build deck: values 2–14 (where 11=Jack, 12=Queen, 13=King, 14=Ace)
deck = [{'value': i, 'suit': c}
        for c in suits
        for i in range(2, 15)]

# Check length
print("Number of cards:", len(deck))   # 52

# Access first card
print("First card suit:", deck[0]['suit'])
print("First card value:", deck[0]['value'])

# Example: print first 5 cards
for card in deck[:5]:
    print(card)
