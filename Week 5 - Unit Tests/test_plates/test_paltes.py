from plates import is_valid

# Test for invalid letters after numbers
def test1():
    assert is_valid('ab23a5') == False

# Test for invalid first letters
def test2():
    assert is_valid('0ab232') == False
    assert is_valid('a02356') == False
    assert is_valid('ab2345') == True
    assert is_valid('12345') == False

# Test for invalid length
def test3():
    assert is_valid('a') == False

# Test for invalid alphanumeric characters
def test4():
    assert is_valid('asd2356')==False

# Test for invalid zero placement
def test5():
    assert is_valid('asd032') == False

# Test for invalid special characters
def test6():
    assert is_valid('ab@%#')== False

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

if __name__ == "__main__":
    main()
