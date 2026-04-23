from random import randint # import function
secret_num = randint(1,100) #assign random number
num_guesses = 0 #define var
guess = 0 # define var

while guess != secret_num and num_guesses <= 9: # True & True
    guess = eval(input('Enter your guess (1-100): ')) # Ask user about guess
    num_guesses = num_guesses + 1 #increment no of guesses
    if guess < secret_num:
        print('HIGHER.', 10-num_guesses, 'guesses left.')
    elif guess > secret_num:
        print('LOWER.', 10-num_guesses, 'guesses left.')
    else:
        print('You got it!')
        
if num_guesses==10 and guess != secret_num: #False and False
    print('You lose. The correct number is', secret_num)
