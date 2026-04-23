from string import punctuation
text = open('romeoandjuliet.txt').read()
text = text.lower()
for p in punctuation:
    text = text.replace(p,'')
words = text.split()
print(words)

d = {}

for w in words:
    if w in d:
     d[w] = d[w] + 1
    else:
     d[w] = 1
# alphabetical order
items = list(d.items())
print(items)

items.sort()
# least to most common
items = [(i[1], i[0]) for i in items]
items.sort()

print(items)
