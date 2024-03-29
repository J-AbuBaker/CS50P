def get_fraction():
    while True:
        fraction = input('Fraction: ').split('/')
        try:
            x, y = int(fraction[0]), int(fraction[-1])
            if x > y:
                continue
        except ValueError:
            continue
        else:
            return f'{x}/{y}'

def convert(fraction):
    fraction = fraction.split('/')
    try:
        x, y = int(fraction[0]), int(fraction[1])  # Convert numerator and denominator to integers
        percentage = round(x / y * 100)
    except ValueError:
        raise ValueError("Invalid fraction")  # Raise ValueError for invalid input
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero")
    return int(percentage)



def gauge(percentage):
    if percentage >= 0 and percentage <= 1:
        return 'E'
    elif percentage >= 99 and percentage <= 100:
        return 'F'
    else:
        return f'{percentage}%'

def main():
    fraction = get_fraction()
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)

if __name__ == '__main__':
    main()
