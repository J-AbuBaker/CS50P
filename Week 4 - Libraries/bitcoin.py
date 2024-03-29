import sys
import requests

try:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    usd = response['bpi']['USD']
    usd_rate = float(usd['rate'].replace(',', ''))
except requests.RequestException as request_err:
    pass
try:
    if len(sys.argv) == 0:
        sys.exit('Missing command-line argument')
    n = float(sys.argv[1])
except ValueError as err:
    sys.exit('Command-line argument is not a number')

cost = round((usd_rate * n), 4)
print(f'${cost:,}')
