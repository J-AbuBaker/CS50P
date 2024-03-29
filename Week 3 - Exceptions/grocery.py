items = []
while True:
    try:
        items.append(input().upper().strip())
    except EOFError:
        break

items_dict = {}
for item in items:
    items_dict[item] = items_dict.get(item, 0) + 1

# Sort the dictionary by keys
sorted_items_dict = sorted(items_dict.items())

for k, v in sorted_items_dict:
    print(f'{v} {k}')
