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
        self.items = []

    def __str__(self):
        str = f'''\n--------------------------------'
                  \n{self.name}
                  \n  {self.description}\n
                  \n{self.get_paths()}\n
                  {self._get_item_string()}'''
        return str

    def __repr__(self):
        return f'Room({self.name}, {self.description})'

    def _get_item_string(self):
        if len(self.items) > 0:
            return '\nItems in room:\n\n     ' + ', '.join([item.name for item in self.items]) + '\n'
        else:
            return ''

    def get_paths(self):
        paths = []
        if self.n_to is not None:
            paths.append('n')
        if self.s_to is not None:
            paths.append('s')
        if self.e_to is not None:
            paths.append('e')
        if self.w_to is not None:
            paths.append('w')
        return 'Paths: ' + ', '.join(paths)


# room_1 = Room('Testing', 'This room is for testing purposes')
# print(room_1)
# print(repr(room_1))
