import random
numbers = [1,2,3,4,5,6,7,8,9,10]
# print('Game Start and Gauss a number 1-9')
# print('*'*35)

computer_number = random.choice(numbers)
while True:
    number = int(input('What is you guess: '))
    if computer_number == number:
        print('Congratulations')
        break
    else:
        print('Hoye nai tor guessing number')