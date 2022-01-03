print('Caculator!')
while True:
    number1 = int(input('Number: '))
    number2 = int(input('Number: '))
    idk = input('x,+,-,/: ')
    if idk == 'x':
        print(number1 * number2)
    elif idk == '+':
        print(number1 + number2)
    elif idk == '-':
        print(number1 - number2)
    elif idk == '/':
        print(number1 / number2)
    else: 
        print('Invalid')
