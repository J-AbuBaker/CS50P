greeting = input('Greeting:').lower().strip().replace(',', '')
if greeting.startswith('hello'):
    print('$0')
elif greeting[0] == 'h':
    print('$20')
else:
    print('$100')
