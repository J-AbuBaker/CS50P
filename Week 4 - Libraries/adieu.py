import inflect
p = inflect.engine()
names = []

while True:
    try:
        name = input('Name: ')
    except EOFError as err:
        break
    else:
        names.append(name)


names_txt = p.join(names)
print(f'Adieu, adieu, to {names_txt}')
