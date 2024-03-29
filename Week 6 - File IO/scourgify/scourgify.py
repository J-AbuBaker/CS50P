import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
    sys.exit('Not a csv file')

try:
    before = sys.argv[1]
    after = sys.argv[2]
    with open(before, 'r') as read, open(after, 'w', newline='') as write:
        lines_to_write = ['first,last,house\n']
        lines = read.readlines()
        if len(lines) == 0:
            sys.exit('Input file is empty')

        header = lines[0].strip().split(',')
        if len(header) < 2:
            sys.exit('Invalid CSV format: Header must contain at least two columns')

        writer = csv.writer(write)
        writer.writerow(['first', 'last', 'house'])

        for line in lines[1:]:
            line = line.strip().replace('"', '')
            fields = line.split(',')
            if len(fields) < 2:
                print(f"Skipping line: {line.strip()} - Missing required fields")
                continue

            last_name, first_name, house = fields[0].strip(), fields[1].strip(), fields[2].strip()

            writer.writerow([first_name, last_name, house])

    print(f"Processing complete. Result saved to '{after}'")

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
except Exception as e:
    sys.exit(f"An error occurred: {str(e)}")
