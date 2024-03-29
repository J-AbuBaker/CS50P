import pytest
from working import convert

def test_valid_conversion():
    assert convert("10:30 AM to 3:45 PM") == "10:30 to 15:45"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:45 PM") == "12:30 to 13:45"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("10:30 AM - 3:45 PM")  # Wrong delimiter
    with pytest.raises(ValueError):
        convert("10:30 AM 3:45 PM")     # Missing 'to'
    with pytest.raises(ValueError):
        convert("10:30 AM 3:45 PM to")  # Missing second time

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:30 AM to 3:45 PM")  # Hours out of range
    with pytest.raises(ValueError):
        convert("10:70 AM to 3:45 PM")  # Minutes out of range

def test_period_conversion():
    assert convert("11:30 PM to 1:45 AM") == "23:30 to 01:45"
    assert convert("1:30 AM to 1:45 PM") == "01:30 to 13:45"

def test_edge_cases():
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    assert convert("12:00 PM to 11:59 AM") == "12:00 to 11:59"
