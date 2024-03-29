import random

NUM_QUESTIONS = 10
MAX_TRIES = 3


def main():
    level = get_level()
    score = 0
    for _ in range(NUM_QUESTIONS):
        x, y = generate_integer(level)
        tries = MAX_TRIES
        while tries != 0:
            try:
                user_input = int(input(f'{x} + {y} = '))
                result = x + y
                if user_input == result:
                    score += 1
                    break
                else:
                    print(f'{x} + {y} = EEE')
                    tries -= 1
            except ValueError:
                print('EEE')
        else:
            print(f'{x} + {y} = {result}')
    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
