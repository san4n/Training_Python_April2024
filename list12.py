questions = ['Capital of France?','State with one neighbor?']
answers = ['Paris', 'Maine']

for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower()==answers[i].lower():
        print('Correct')
    else:
        print('Answer:', answers[i])
