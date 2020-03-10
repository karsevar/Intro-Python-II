# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name):
        self.current_room = None 
        self.name = name 
        self.items = []

    def move(self, direction):
        print(getattr(self.current_room, direction))
        if type(getattr(self.current_room, direction)) != str:
            self.current_room = getattr(self.current_room, direction)

    def __str__(self):
        return f'character name: {self.name}, current_room: {self.current_room}'
