import pandas as pd
import numpy as np
class Item:

    def __init__ (self, id=0, name='store', price=0):
        self.id = id
        self.name = name
        self.price = price

    def id_item(self):
        return {
            'id': self.id,
            'item_name': self.name,
            'price': self.price
        }

    def id_generator(self,csv_file):
        data = pd.read_csv(csv_file).sort_values('id')
        self.id = 1
        for i in data['id']:
            if i == self.id:
                self.id = self.id + 1
            else:
                break
        return self.id

class Store:

    def __init__(self, id =1, item_name=None, price=0, pieces=0):
        self.id = id
        self.item_name = item_name
        self.price = price
        self.pieces = pieces

    def add_item(self):                                                                                                                                 
        self.id = Item().id_generator('items.csv')
        item = Item(self.id, self.item_name, self.price).id_item()
        df = pd.DataFrame([item])
        df.to_csv('items.csv', mode='a', index=False, header=False)
        print(self.item_name, 'Successfully Added.')
    
    def remove_item(self):
        items_list = pd.read_csv('items.csv')
        check = items_list[items_list['item_name'] == self.item_name]
        if check.empty:
            print('No', self.item_name, 'in the list.')
        else:
            print(check)
            while True:
                id = int(input('Enter ID: '))
                if items_list[items_list['id'] == id].empty:
                    print('No ID Found')
                else: 
                    break
            items_list = items_list.values
            count = 0
            for i in items_list:
                if i[0] == id:
                    items_list = np.delete(items_list,count,axis=0)
                    break
                count += 1
            df = pd.DataFrame(items_list, columns=['id', 'item_name', 'price'])
            df.to_csv('items.csv', index=False)

    def buy_item(self):
        data = pd.read_csv('items.csv')
        if data[data['item_name'] == self.item_name].empty:
            return 'No ', self.item_name, 'in the list.' 
        else:
            print(data[data['item_name'] == self.item_name])
            self.id = int(input('Enter ID: '))
            item = data[data['id'] == self.id].values
            total_price = item[0][2] * self.pieces
            return total_price

    def display_item(self):
        data = pd.read_csv('items.csv').sort_values('id').set_index('id')
        return data
        

            