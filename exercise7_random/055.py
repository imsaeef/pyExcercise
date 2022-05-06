import random
num = random.randint(1,5)
guess = int(input('ENter a number: '))
if guess == num:
    print('Well done')
elif guess > num:
    print('too high')
    guess = int(input('guess again: '))
    if guess == num:
        print('correct')
    else:
        print('you lose')
elif guess < num:
    print('too low')
    guess = int(input('guess again: '))
    if guess == num:
        print('correct')
    else:
        print('you lose')
