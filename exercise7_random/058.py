import random
score = 0
for i in range(1,6):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    correct = num1+num2
    print(num1,'+',num2,'= ')
    answer = int(input('your answer: '))
    print()
    if answer == correct:
        score = score + 1
print('you got',score,'out of 5')
