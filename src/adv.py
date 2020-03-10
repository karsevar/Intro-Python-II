from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

print(room['outside'].n_to)

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
user_input = 0
current_room = room['outside']

while user_input != 'q':
    user_input = input('\nPlease pick one of the four direction commands [n, s, e, or w] or q to quit\n')
    if user_input == 'n':
        print(current_room.n_to)
        if type(current_room.n_to) != str:
            current_room = current_room.n_to
    elif user_input == 's':
        print(current_room.s_to)
        if type(current_room.s_to) != str:
            current_room = current_room.s_to
    elif user_input == 'w':
        print(current_room.w_to)
        if type(current_room.w_to) != str:
            current_room = current_room.w_to
    elif user_input == 'e':
        print(current_room.e_to)
        if type(current_room.e_to) != str:
            current_room = current_room.e_to