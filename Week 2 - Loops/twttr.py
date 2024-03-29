txt = input('Input: ')
out = ''
vowels = ['a', 'e', 'o', 'i', 'u']
for ch in txt:
    if ch.lower() not in vowels:
        out += ch
print(f'Output: {out}')

