# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def __str__(self):
        return f'{self.name} is in room: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'

    def move_player(self, direction):
        # Check if theres a valid room in the direction
        # if so, update the current room to new room and print description
        # Else print an error message
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            print('Sorry! Unable to go that way.', '\n')

# player_1 = Player(1)
# print(player_1)
# print(repr(player_1))
