from datetime import datetime
from seasons import get_age_in_minutes_string, get_birth_date_from_user
import pytest
import sys

def success_test():
    birth_date_1 = datetime.strptime('2021-08-12', '%Y-%m-%d').date()
    birth_date_2 = datetime.strptime('2020-08-12', '%Y-%m-%d').date()
    assert get_age_in_minutes_string(birth_date_1) == 'One million, three hundred seventy-nine thousand, five hundred twenty minutes'
    assert get_age_in_minutes_string(birth_date_2) == 'One million, nine hundred five thousand, one hundred twenty minutes'

def fail_test():
    with pytest.raises(SystemExit):
        with pytest.raises(ValueError):
            get_birth_date_from_user()


def test_calculate_age_in_minutes():
    # Test case 1: Birth date is today
    today = date.today()
    assert calculate_age_in_minutes(today) == 0

    # Test case 2: Birth date is one day ago
    one_day_ago = today - timedelta(days=1)
    assert calculate_age_in_minutes(one_day_ago) == 24 * 60

    # Test case 3: Birth date is one year ago
    one_year_ago = today.replace(year=today.year - 1)
    expected_minutes = 365 * 24 * 60
    assert calculate_age_in_minutes(one_year_ago) == expected_minutes

    # Test case 4: Birth date is one year and one day ago (leap year)
    one_year_one_day_ago = one_year_ago - timedelta(days=1)
    expected_minutes = 365 * 24 * 60 + 24 * 60
    assert calculate_age_in_minutes(one_year_one_day_ago) == expected_minutes

    # Test case 5: Birth date is in the future (should return negative minutes)
    future_date = today.replace(year=today.year + 1)
    assert calculate_age_in_minutes(future_date) < 0

def main():
    success_test()
    fail_test()
    test_calculate_age_in_minutes()
if __name__ == '__main__':
    main()
