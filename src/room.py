# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name 
        self.description = description
        self.items = items 
        self.n_to = f'Error: There is not a room north of {self.name}'
        self.s_to = f'Error: There is not a room south of {self.name}'
        self.e_to = f'Error: There is not a room east of {self.name}'
        self.w_to = f'Error: There is not a room west of {self.name}'

    def loss_item(self, item):
        for item_index in range(len(self.items)):
            if self.items[item_index].name == item:
                self.items[item_index].on_take()
                return self.items.pop(item_index)
        return f'item {item} not found in room {self.name}'
    
    def show_inventory(self):
        print(f'Items in room {self.name}:')
        for item in self.items:
            print(f'{item}')

    def reclaim_item(self, item):
        

    def __str__(self):
        if len(self.items) > 0:
            return f'name: {self.name}\ndescription: {self.description}\nItems In Room: {self.items}'
        else:
            return f'name: {self.name}\ndescription: {self.description}\nItems In Room: No Items'

    