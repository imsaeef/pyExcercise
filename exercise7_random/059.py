import random
color = random.choice(['red','green','blue','pink','white'])
print('select from red,green,blue,pink or white')
again = True
while again == True:
    chose = input('Enter a color: ').lower()
    if color == chose:
        print('Well done')
        again = False
    else:
        if color == 'red':
            print('I bet you are seeing RED right now')
        elif color == 'green':
            print('I bet you are GREEN roight now')
        elif color == 'blue':
            print('You are probably feeling BLUE right now')
        elif color == 'pink':
            print('shame you are not feeling in the PINK, as you got it wrong!')
        elif color == 'white':
            print("are you WHITE as a sheet, as you didn't guess correctly")
