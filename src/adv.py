from room import Room
from player import Player
from item import Item
import textwrap

# Declaring all items:
items = {
    'sword': Item('sword', 'magic sword for slaying loneliness'),
    'shield': Item('shield', 'normal shield for protection against humans'),
    'map': Item('map', 'for when the travelers are lost.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items['sword'], items['map']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['shield']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['map']]),
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

# helper function that evaluates whether there is a room in user 
# specified direction:
#def has_room():

# Pick the name of the character in the game.
player_name = input('Before you proceed, please type in a name for your player! ')

# Initial room variable:
current_room = room['outside']

print(current_room.n_to)

# initializes the Player class with user inputted name and initial room (cave entrance)
character = Player(player_name, room['outside'])

print(f'\nCurrent room: name {current_room.name}\n description {current_room.description}\n')

while True:

    current_room.show_items()

    user_input = input('\nPlease enter a direction you want the player to move. Selections include: [n, s, e, w]! ')

    user_input = user_input.split(' ')

    if len(user_input) == 1:

        if user_input[0] in ['n','s','w','e']:
            character.move(user_input[0])
            current_room = character.current_room

        elif user_input[0] in ['i', 'inventory']:
            character.show_inventory()

        elif user_input[0] == 'q':
            print('Goodbye!!!')
            break

        else:
            print('\nPlease use the valid inputs [n, s, e, w] to move, drop [item] and take [item], i to check inventory, or q to quit\n')

    elif len(user_input) == 2:

        if user_input[0] == 'take':

            if current_room.search_item(user_input[1]):
                acquired_item = current_room.lose_item(user_input[1])
                acquired_item.on_take()
                character.pickup_item(acquired_item)

            else:
                print(f'\nCan\'t find item {user_input[1]} in room {current_room.name}\n')

        elif user_input[0] == 'drop':
            
            if character.search_inventory(user_input[1]):
                reclaim_item = character.drop_item(user_input[1])
                current_room.restock_item(reclaim_item)

            else:
                print(f'\nCan\'t find item {user_input[1]} in inventory\n')

        else:
            print('\nPlease use the valid inputs [n, s, e, w] to move, drop [item] and take [item], i to check inventory, or q to quit\n')

    elif len(user_input) > 2:
        print('User input exceeded input limit. Maximum input accepted 2 words')