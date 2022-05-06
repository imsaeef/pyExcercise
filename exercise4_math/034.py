print("1) Square")
print("2) Triangle")
print()

user = int(input("Enter a number: "))
if user == 1:
    side = int(input('Enter the length of one side: '))
    area = side*side
    print("The area of your chosen shape is", area)
elif user == 2:
    base = int(input('Enter the base of triangle: '))
    height = int(input('Enter the height of triangle: '))
    area = (base*height)/2
    print("The area of your chosen shape is", area)
else:
    print('Your selection is Invalid!!')
