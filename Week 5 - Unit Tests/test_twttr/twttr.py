def main():
    word = input('Input: ')
    print(f'Output: {shorten(word)}')



def shorten(word):
    new_word = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in word:
        if ch.lower() not in vowels:
            new_word += ch
    return new_word

if __name__ == "__main__":
    main()
