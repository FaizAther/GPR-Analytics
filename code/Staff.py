from IdClass import IdClass
from User import User
from StaffType import StaffType
'''
    Staff Class
'''

class Staff(User):

    def __init__(self, id, type):
        super().__init__(id)
        self._type = type