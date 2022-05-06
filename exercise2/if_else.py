num1 = int(input())

# solution 1
# if num1 > 10:
#     print('This is over 10')
# elif num1 == 10:
#     print('This is equal 10')
# else:
#     print('this is under 10')

# solution 2
if num1 >= 10:
    if num1 > 10:
        print('this is over')
    else:
        print('this is equal')
else:
    print('this is under')
    