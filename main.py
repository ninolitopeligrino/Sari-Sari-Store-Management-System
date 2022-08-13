import objects
import pandas as pd
store = objects.Store
while True:
    print('Sari-Sari Store Management System')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Buy Item')
    print('4. Display Item')
    choice = input('Enter your Choice: ')
    if choice == '0':
        break
    elif choice == '1':
        name = input('Name of Item: ')
        price = int(input('Enter price: '))
        store(item_name=name, price=price).add_item()
    elif choice == '2':
        name = input('Enter Item Name to remove: ')
        store(item_name=name).remove_item()
    elif choice == '3':
        name = input('Enter item name: ')
        piece = int(input('Enter Number of {}: '.format(name)))
        print('Total: ',store(item_name=name, pieces=piece).buy_item())
    elif choice == '4':
        print(store().display_item())
    else:
        print('Choose properly')