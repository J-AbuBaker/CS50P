inp = input('What is the Answer to the Great Question of Life, the Universe, and Everything?').lower()
ans = ['42', 'forty-two', 'forty two']
if inp in ans:
    print('Yes')
else:
    print('No')
