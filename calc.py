while True:
    print('Enter \'add\' for addition')
    print('Enter \'sub\' for subtraction')
    print('Enter \'mul\' for multiplication')
    print('Enter \'div\' for division')
    print('Enter \'quit\' to quit')

    command = input()
    if command == 'quit':
        break

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    if command == 'add':
        print(float(num1) + float(num2))
    elif command == 'sub':
        print(float(num1) - float(num2))
    elif command == 'mul':
        print(float(num1) * float(num2))
    elif command == 'div':
        print(float(num1) / float(num2))
    else:
        print('Crappy Input')
    print('\n ************************\n')
