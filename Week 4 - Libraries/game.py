import random
import sys

def get_n():
    while True:
        try:
            n = int(input('Level: '))
            if n > 0:
                return n
        except ValueError:
            continue

def guess():
    random_guess = random.randint(1, get_n())

    while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0:
                if guess == random_guess:
                    print('Just right!')
                    sys.exit()
                elif guess < random_guess:
                    print('Too small!')
                else:
                    print('Too large!')
        except ValueError:
            continue

def main():
    guess()

if __name__ == '__main__':
    main()
