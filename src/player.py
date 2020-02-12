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

# player_1 = Player(1)
# print(player_1)
# print(repr(player_1))
