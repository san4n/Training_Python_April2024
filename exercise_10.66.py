# Print a 10x10 grid using two loops
for i in range(1, 11):        # rows
    for j in range(1, 11):    # columns
        print("{:3d}".format(j), end=" ")
    print()  # move to next line after each row

#------------

# Find primitive Pythagorean triples (x, y, z) under 100 without gcd
triples = []

for x in range(1, 100):
    for y in range(x+1, 100):        # y > x avoids duplicates like (3,4,5) vs (4,3,5)
        for z in range(y+1, 100):    # z > y ensures ordered triples
            if x*x + y*y == z*z:
                # Check if (x,y,z) is not a multiple of a smaller triple
                is_multiple = False
                for (a, b, c) in triples:
                    if x % a == 0 and y % b == 0 and z % c == 0:
                        is_multiple = True
                        break
                if not is_multiple:
                    triples.append((x, y, z))

# Print results
print("Primitive Pythagorean triples under 100:")
for t in triples:
    print(t)

#-----------


