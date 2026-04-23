n = eval(input("Enter frist number: "))
m = eval(input("Enter second number: "))

print(f"Frist Number {n}, Second Number {m}")

z = n # Temp Variable to store n
n = m
m = z

print(f"First NUmber {n}, Second NUmber {m}")

#Shortcut
a = 6
b = 5

a,b = b,a #swap

print(a)
print(b)
