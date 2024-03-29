name = input('camelCase: ')
sanke_case = ''
for ch in name:
    if ch.isupper():
        sanke_case += '_' + ch.lower()
    else:
        sanke_case += ch
print(f'snake_case: {sanke_case}')
