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
            print('\nYou are carrying:\n  ' +
                  ', '.join([item.name for item in self.items]) + '\n')
        else:
            print('\nYou have 0 items\n')

    def get_item(self, item_to_get):
        items_in_room = [item.name.lower() for item in self.current_room.items]
        if item_to_get in items_in_room:
            for item in self.current_room.items:
                if item.name.lower() == item_to_get:
                    player_item = item
                    self.items.append(player_item)
                    print(f'\nYou aquired a {player_item.name}\n')
                    self.current_room.items.remove(player_item)

    # WIP
    def drop_item(self, item_to_drop):
        player_items = [item.name.lower() for item in self.items]
        if item_to_drop in player_items:
            for item in self.items:
                if item.name.lower() == item_to_drop:
                    self.current_room.items.append(item)
                    self.items.remove(item)
                    print(f'\nYou dropped {item.name}\n')
