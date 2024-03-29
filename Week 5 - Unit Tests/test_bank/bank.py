def value(greeting):
    if greeting.startswith('hello'):
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

def main():
    greeting = input('Greeting:').lower().strip().replace(',', '')
    val = value(greeting)
    print(f'%{val}')



if __name__ == "__main__":
    main()
