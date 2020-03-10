from room import Room
from player import Player
from item import Item

# Declare all items:
items = {
    'sword': Item('Sword', 'The Sword that cuts through fear!'),
    'shield': Item('Shield', 'The shield the protects against fear!'),
    'map': Item('Map', 'Helps you find your way!'),
    'flashlight': Item('Flashlight', 'Portable light'),
    'potion': Item('Potion', 'Restores 50 HP points.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword'], items['map']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['shield']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['flashlight']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['potion']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# initial input for the REPL.

print('Welcome to the text room adventure game!!!\n')
player_name = input('Please enter a name for your player!\n')
character = Player(player_name)
user_input = 0
character.current_room = room['outside']

while user_input != 'q':
    user_input = input('\nPlease pick one of the four direction commands [n, s, e, or w],\nuse the phrase commmand take [item] or drop [item],\nor q to quit\n')
    user_input = user_input.split(' ') 
    if len(user_input) == 1:
        user_input = user_input[0]
        if user_input == 'n':
            character.move('n_to')
        elif user_input == 's':
            character.move('s_to')
        elif user_input == 'w':
            character.move('w_to')
        elif user_input == 'e':
            character.move('e_to')
        elif user_input == 'i':
            character.show_inventory()
        elif user_input == 'q':
            print('\n~~~~~~GoodBye~~~~~~~~\n')
        else:
            print('\n~~~~~Invalid Command~~~~~\n')
    elif len(user_input) == 2:
        verb = user_input[0]
        item = user_input[1]
        if verb == 'take':
            character.take_item(item)
        # elif verb == 'drop':


    else:
        print('\n~~~~~Invalid Command Length~~~~~~~~\n')

    