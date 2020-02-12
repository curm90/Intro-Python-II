# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        str = print(f'\n--------------------------------')
        str += print(f'\n{self.name}\n  {self.description}\n')
        return str

    def __repr__(self):
        return f'Room({self.name}, {self.description})'


# room_1 = Room('Testing', 'This room is for testing purposes')
# print(room_1)
# print(repr(room_1))
