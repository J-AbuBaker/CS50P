while True:
    months = {
        "January": '01',
        "February": '02',
        "March": '03',
        "April": '04',
        "May": '05',
        "June": '06',
        "July": '07',
        "August": '08',
        "September": '09',
        "October": '10',
        "November": '11',
        "December": '12'
    }

    try:
        date = input('Date: ').title()
        if '/' in date:
            date_iso_8601 = date.split('/')
            year = int(date_iso_8601[-1])
            month = int(date_iso_8601[0])
            day = int(date_iso_8601[1])
            if day < 1 or day > 31 or month < 1 or month > 12:
                raise ValueError()
        elif ', ' in date:
            date_parts = date.split(' ')
            month = months[date_parts[0]]
            day = int(date_parts[1][:-1])  # Remove the comma from the day part
            year = int(date_parts[2])
            if day < 1 or day > 31 or month not in months.values():
                raise ValueError()
        else:
            raise ValueError()

        print(f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}')
        break

    except ValueError:
        pass
    except KeyError:
        pass
