from fuel import convert, gauge
import pytest

def test_convert():
    # Test valid conversions
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('1/100') == 1

    # Test invalid conversions - ValueError
    with pytest.raises(ValueError):
        convert('cat/dog')

    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge():

    assert gauge(1) == "E"
    assert gauge(0) == "E"

    assert gauge(99) == "F"
    assert gauge(100) == "F"

    assert gauge(75) == '75%'
    assert gauge(25) == '25%'


if __name__ == "__main__":
    test_convert()
    test_gauge()
