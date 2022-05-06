again = 'y'
count = 0
while again == 'y':
    name = input('enter a name somebody you want to ivite to your party: ')
    print(name,'has now been invited')
    count = count + 1
    again = input('do you want to invite somebody else? y/n: ')
print(count,'people coming to your party')