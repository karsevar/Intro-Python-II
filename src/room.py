# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):

        self.name = name 
        self.description = description
        self.n_to = 'Sorry there is no room north of {}\n'.format(self.name)
        self.s_to = 'Sorry there is no room south of {}\n'.format(self.name)
        self.e_to = 'Sorry there is no room east of {}\n'.format(self.name)
        self.w_to = 'Sorry there is no room west of {}\n'.format(self.name)
        self.items = items

    def search_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return True 
        return False

    def show_items(self):
        if len(self.items) > 0:
            print(f'\nItems in {self.name}:')
            # print(item_array[0])
            for item in self.items:
                print(item)
        else:
            print(f'\nNo items in {self.name}.')

    def restock_item(self, item):
        self.items.append(item)

    def lose_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return self.items.pop(self.items.index(item_name))

    def __str__(self):
        return str(self.__dict__)