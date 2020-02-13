from room import Room
from player import Player
from item import Item

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

sword = Item('Sword', 'An old rusty sword')
book = Item('Book', 'A book about treasure')
rock = Item('Rock', 'This is a rock')
key = Item('Key', 'I wonder what this could be used for')
lighter = Item('Lighter', 'This could come in handy')

room['outside'].items.append(rock)
room['foyer'].items.append(lighter)
room['overlook'].items.append(book)
room['narrow'].items.append(key)
room['treasure'].items.append(sword)


player_1 = Player('Liam', room['outside'])

current_room = player_1.current_room

print(current_room)

directions = ['n', 's', 'e', 'w']

while True:
    user_input = input('--> ')

    if user_input in directions:
        player_1.move_player(user_input)
    elif user_input == 'i':
        player_1.print_inventory()
    elif user_input == 'q':
        print('Goodbye!')
        exit()
    else:
        print('I did not recognise that command')
