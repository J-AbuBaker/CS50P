import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')

try:
    file_name = sys.argv[1]
    with open(file_name) as file:
        lines = file.readlines()
        rows = []
        for line in lines:
            row = line.strip().split(',')
            rows.append(row)
        headers = rows[0]
        table = rows[1:]
        print(tabulate(table, headers, tablefmt='grid'))
except FileNotFoundError:
    sys.exit('File does not exist')
