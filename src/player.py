# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):

        self.name = name
        self.current_room = current_room
        self.items = []

    def show_inventory(self):
        if len(self.items) > 0:
            print(f'\n{self.name}\'s item inventory: ')
            for item in self.items:
                print(item)
        else:
            print(f'\nCharacter {self.name} needs items!')

    def drop_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                reclaim_item = self.items.pop(self.items.index(item_name))
                self.current_room.restock_item(reclaim_item)
                return f'{reclaim_item.name} has been returned to room {self.current_room.name}'

        return f'\nCan\'t find item {item} in inventory\n'

    def move(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to')
        if isinstance(next_room, str):
            print(f'\n~~~~Error~~~~~\n')
            print(next_room)
        else:
            self.current_room = next_room
            print(f'\nCurrent room: name {next_room.name}\n description {next_room.description}\n')

    def pickup_item(self, item):

        if self.current_room.search_item(item):
            acquired_item = self.current_room.lose_item(item)
            print(acquired_item)
            acquired_item.on_take()
            self.items.append(acquired_item)
        else: 
            print(f'\nCan\'t find item {item} in room {self.current_room.name}\n')

    def __str__(self):
        return str(self.__dict__) 
