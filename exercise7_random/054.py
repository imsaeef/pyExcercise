import random
coin = random.choice(['h','t'])
guess = input('pick (h)eads or (t)ails: ')
if guess == coin:
    print('you win')
else:
    print('bad luck')
if coin == 'h':
    print('it was heads')
else:
    print('it was tails')
