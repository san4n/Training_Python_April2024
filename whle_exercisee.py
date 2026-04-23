import random

# 01 Setup
secret_num = random.randint(1, 50)   # generate secret number between 1 and 50
num_guesses = 0
guess = 0

# 02 Loop Condition
while guess != secret_num and num_guesses <= 4:
    guess = int(input("Enter your guess: "))
    num_guesses += 1
    
    # 03 Higher/Lower feedback
    if guess < secret_num:
        print("HIGHER! Remaining guesses:", 5 - num_guesses)
    elif guess > secret_num:
        print("LOWER! Remaining guesses:", 5 - num_guesses)
    else:
        print("Correct! You guessed it in", num_guesses, "tries.")

# 04 End Message
if num_guesses == 5 and guess != secret_num:
    print("Sorry, you've used all 5 tries.")
    print("The correct number was:", secret_num)
