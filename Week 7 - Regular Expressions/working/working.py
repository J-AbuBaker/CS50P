
import re

def main():
    print(convert(input("Hours: ")))

def convert(time):
    try:
        match = re.search(r'(\d{1,2}?:?\d{0,2}?) (\w+) to (\d{1,2}?:?\d{0,2}?) (\w+)', time)
        if not match:
            raise ValueError()

        time_from = [*map(int, match.group(1).split(':')), match.group(2)]
        time_to = [*map(int, match.group(3).split(':')), match.group(4)]

        if len(time_from) == 3:
            hours_from = time_from[0]
            minutes_from = time_from[1]
            period_from = time_from[-1]
        else:
            hours_from = time_from[0]
            minutes_from = 0
            period_from = time_from[-1]

        if len(time_to) == 3:
            hours_to = time_to[0]
            minutes_to = time_to[1]
            period_to = time_to[-1]
        else:
            hours_to = time_to[0]
            minutes_to = 0
            period_to = time_to[-1]

        if not (0 <= hours_from <= 12 and 0 <= hours_to <= 12 and 0 <= minutes_from < 60 and 0 <= minutes_to < 60):
            raise ValueError

        if 'AM' in time_from and hours_from == 12:
            hours_from = 0
        if 'PM' in time_to and hours_to == 12:
            hours_to = 0

        if period_from == 'PM' and hours_from != 12:
            hours_from += 12
        elif period_to == 'PM' and hours_to != 12:
            hours_to += 12

        start_time = f'{hours_from:02}:{minutes_from:02}'
        end_time = f'{hours_to:02}:{minutes_to:02}'
        return f'{start_time } to {end_time}'
    except ValueError:
        raise ValueError
    except AttributeError:
        raise ValueError

if __name__ == "__main__":
    main()

