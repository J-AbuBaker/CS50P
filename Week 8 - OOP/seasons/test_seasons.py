from seasons import convert
import pytest
import sys

def test_good():
    assert convert('2021-08-12') == 'Five hundred twenty-five thousand, six hundred minutes'
    assert convert('2020-08-12') == 'One million, fifty-one thousand, two hundred minutes'

def test_bad():
    with pytest.raises(SystemExit):
        convert('2020-8-12')

def main():
    test_good()
    test_bad()
    sys.exit(0)
