from bank import value

def test_hello():
    assert value('Hello') == 0
    assert value('Hello, Newman') == 0

def test_starting_with_h():
    assert value('How you doing?') == 20

def test_default():
    assert value("What's happening?") == 100

def main():
    test_hello()
    test_starting_with_h()
    test_default()

if __name__ == '__main__':
    main()
