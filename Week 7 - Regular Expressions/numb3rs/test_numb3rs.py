from numb3rs import validate

def test_valid_ipv4():
    assert validate('192.168.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_invalid_ipv4():
    assert validate('256.256.256.256') == False
    assert validate('300.200.100.50') == False
    assert validate('abc.def.ghi.jkl') == False
    assert validate('192.168.0') == False

def test_edge_cases():
    assert validate('') == False
    assert validate('1.1.1') == False
    assert validate('1.1.1.1.1') == False

def test_mixed_cases():
    assert validate('192.168.0.1') == True
    assert validate('127.0.0.1') == True
    assert validate('300.400.500.600') == False

if __name__ == '__main__':
    test_valid_ipv4()
    test_invalid_ipv4()
    test_edge_cases()
    test_mixed_cases()
    print("All tests passed successfully!")
