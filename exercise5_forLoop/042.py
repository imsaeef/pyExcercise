total = 0

for i in range(5):
    num = int(input('Enter a number: '))
    reply = input('You want to included your number? y/n: ')
    if reply == 'y':
        total = total + num
print(total)
