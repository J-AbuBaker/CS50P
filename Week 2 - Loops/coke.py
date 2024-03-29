amount_due = 50
total = 0

while amount_due > 0:
    print(f'Amount Due: {amount_due}')
    coin = int(input('Insert Coin: '))
    coins = [25, 10, 5]
    if coin in coins:
        total += coin
        amount_due -= coin

if  total == 50:
    print('Change Owed: 0')
else:
    print(f'Change Owed: {total - 50}')
