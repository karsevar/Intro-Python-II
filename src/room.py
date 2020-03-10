# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description 
        self.n_to = f'Error: There is not a room north of {self.name}'
        self.s_to = f'Error: There is not a room south of {self.name}'
        self.e_to = f'Error: There is not a room east of {self.name}'
        self.w_to = f'Error: There is not a room west of {self.name}'

    def __str__(self):
        return f'name: {self.name}\ndescription: {self.description}'