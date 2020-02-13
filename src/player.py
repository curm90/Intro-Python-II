# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def __str__(self):
        return f'{self.name} is in room: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'

    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            print('Sorry! Unable to go that way.', '\n')

    def print_inventory(self):
        if len(self.items) > 0:
            print('You are carrying:\n ' +
                  ', '.join([item.name for item in self.items]) + '\n')


# player_1 = Player(1)
# print(player_1)
# print(repr(player_1))
