rain = input('It is raining? ').lower()

if rain == 'yes':
    windy = input('It is windy? ').lower()
    if windy == 'yes':
        print("It's too windy for an umbrella")
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
