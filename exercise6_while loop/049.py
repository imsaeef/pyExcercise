compnum = 50
guess = int(input('enter a number that I am thinking of: '))
count = 1
while guess != compnum:
    if guess < compnum:
        print('too low')
    else:
        print('too high')
    count = count+1
    guess = int(input('guess another number: '))
print('well done,you took',count,'attempts')