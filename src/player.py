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

    def search_inventory(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return True 
        return False

    def drop_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return self.items.pop(self.items.index(item_name))

    def move(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to')
        if isinstance(next_room, str):
            print(f'\n~~~~Error~~~~~\n')
            print(next_room)
        else:
            self.current_room = next_room
            print(f'\nCurrent room: name {next_room.name}\n description {next_room.description}\n')

    def pickup_item(self, item):

        self.items.append(item)

    def __str__(self):
        return str(self.__dict__) 
