from datetime import date
import inflect
import sys

def calculate_age_in_minutes(birth_date):
    today = date.today()
    age = today - birth_date
    total_minutes = age.days * 24 * 60
    return total_minutes

def get_birth_date_from_user():
    try:
        birth_date_str = input("Please enter your date of birth (YYYY-MM-DD): ")
        birth_date = date.fromisoformat(birth_date_str)
        return birth_date
    except ValueError:
        sys.exit("Invalid date format.")

def get_age_in_minutes_string(birth_date):
    age_in_minutes = calculate_age_in_minutes(birth_date)

    # Convert minutes to words using inflect
    p = inflect.engine()
    if age_in_minutes == 1:
        age_in_words = "1 minute"
    else:
        age_in_words = p.number_to_words(age_in_minutes, andword='').capitalize() + " minutes"
    return age_in_words

def main():
    birth_date = get_birth_date_from_user()
    age_string = get_age_in_minutes_string(birth_date)
    print(age_string)

if __name__ == "__main__":
    main()
