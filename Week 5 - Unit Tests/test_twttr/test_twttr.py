from twttr import shorten

def test_shorten():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('What\'s your name?') == 'Wht\'s yr nm?'
    assert shorten('CS50') == 'CS50'
    assert shorten('Ali') == 'l'

def main():
    test_shorten()

if __name__ == '__main__':
    main()
