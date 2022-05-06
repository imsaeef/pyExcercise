invite = int(input('How many people you want to invite to your party? '))

if invite < 10:
    for i in range(0, invite):
        name = input('Enter the name of your guest: ')
        print(name, 'has been invited')
else:
    print('Too many people')
