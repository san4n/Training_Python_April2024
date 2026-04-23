# Using for loop
for i in range(1, 51):
    print(i)

# Equivalent while loop
i = 1
while i < 51:
    print(i)
    i += 1
#-----------------------------#

# kg to lbs conversion factor
KG_TO_LBS = 2.20462

# Ask for weight until valid
weight_kg = float(input("Enter weight in kilograms: "))

while weight_kg <= 0:
    print("Invalid input. Weight must be greater than 0.")
    weight_kg = float(input("Enter weight in kilograms: "))

# Convert to pounds
weight_lbs = weight_kg * KG_TO_LBS
print(f"Weight in pounds: {weight_lbs:.2f}")

#---------------------------

# Set the correct password
correct_password = "secret123"

# Initialize attempt counter
attempts = 0

# Allow up to 5 attempts
while attempts < 5:
    guess = input("Enter password: ")
    attempts += 1
    
    if guess == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Attempts left:", 5 - attempts)

# Lockout message if all attempts fail
if attempts == 5 and guess != correct_password:
    print("Too many failed attempts. You are locked out.")


#---------------


scores = []
count_A = 0

while True:
    score = int(input("Enter score (negative to stop): "))
    if score < 0:
        break
    scores.append(score)
    if score >= 90:
        count_A += 1

# Calculate average if scores exist
if scores:
    average = sum(scores) / len(scores)
    print("Count of A's (≥90):", count_A)
    print("Average score:", round(average, 2))
else:
    print("No scores entered.")

#------------------
