num1 = int(input('enter a number: '))
total = num1
again = 'y'
while again == 'y':
    num2 = int(input('enter another number: '))
    total = total + num2
    again = input('do you want to add another number? y/n: ')
print('the total is: ',total)
