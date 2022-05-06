direction = input('What direction you want to count? up/down: ')

if direction == 'up':
    num1 = int(input('Enter your top number: '))
    for i in range(1, num1+1, 1):
        print(i)
elif direction == 'down':
    num2 = int(input('Enter a number below 20: '))
    for i in range(20, num2-1, -1):
        print(i)
else:
    print("I don't understand")
