from random import randint

num=randint(1,10)
guess = eval(input("Enter your guess: "))

if guess == num:
    print("You are correct.")
else:
    print(f"The number is {num}.")
