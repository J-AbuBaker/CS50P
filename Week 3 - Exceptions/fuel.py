while True:
    try:
        inp = input('Fraction: ').split('/')
        x, y = int(inp[0]), int(inp[-1])
        percentage = (x / y)
        if x > y:
            continue
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        if percentage <= 0.01:
            print('E')
        elif percentage >= 0.99:
            print('F')
        else:
            print(f'{round(percentage * 100)}%')
        break
