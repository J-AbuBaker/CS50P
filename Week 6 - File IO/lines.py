import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')

try:
    file_name = sys.argv[1]
    num_lines = 0
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0 or line.startswith('#') or line.startswith('# '):
                continue
            else:
                num_lines += 1
        print(str(num_lines))
except FileNotFoundError as err:
    sys.exit('File does not exist')
