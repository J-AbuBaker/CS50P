def main():
    time = input('What time is it? ')
    hours = convert(time)
    if hours >= 7 and hours <= 8:
        print('breakfast time')
    elif hours >= 12 and hours <= 13:
        print('lunch time')
    elif hours >= 18 and hours <= 19:
        print('dinner time')
def convert(time):
    return int(time.split(':')[0]) + int(time.split(':')[1]) / 60

if __name__ == '__main__':
    main()
