inp = input('Expression: ')
x = float(inp.split(' ')[0])
y = inp.split(' ')[1]
z = float(inp.split(' ')[-1])
if y == '+' :
    result = x + z
elif y == '-' :
    result = x - z
elif y == '*' :
    result = x * z
elif y == '/':
    result = x / z

print(result)
