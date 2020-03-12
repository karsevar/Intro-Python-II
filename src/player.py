# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name):
        self.current_room = None 
        self.name = name 
        self.items = []

    def move(self, direction):
        print(getattr(self.current_room, f'{direction}_to'))
        if type(getattr(self.current_room, f'{direction}_to')) != str:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            self.current_room.show_inventory()

    def take_item(self, item):
        result = self.current_room.loss_item(item)
        if type(result) != str:
            self.items.append(result)
        else:
            print(result)
    
    def show_inventory(self):
        print(f'\n{self.name}s item inventory:')
        for item in self.items:
            print(item)

    def drop_item(self, item):
        for item_index in range(len(self.items)):
            if self.items[item_index].name == item:
                self.current_room.reclaim_item(self.items.pop(item_index))
                return None
        print(f'Cannot find item {item} in character inventory.')

    def __str__(self):
        return f'character name: {self.name}, current_room: {self.current_room}'


