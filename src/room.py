# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Room: {self.name}\n{self.description}'

    def __repr__(self):
        return f'Room({self.name}, {self.description})'


room_1 = Room('Testing', 'This room is for testing purposes')
print(room_1)
print(repr(room_1))
