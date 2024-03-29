def main() :
    dollars = float(input('How much was the meal? ').replace('$', ''))
    percent = float(input('What percentage would you like to tip? ').replace('%', '')) / 100
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')
main()
