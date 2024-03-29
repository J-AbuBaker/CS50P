from validator_collection import checkers

email = input("What's your email address? ")

if is_email_address := checkers.is_email(email):
    print('Valid')
else:
    print('Invalid')
