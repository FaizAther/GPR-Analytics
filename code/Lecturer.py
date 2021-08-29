from StaffType import StaffType
from User import User
from Staff import Staff
'''
    Lecturer Class
'''

class Lecturer(Staff):
    def __init__(self):
        super().__init__(self, StaffType.LECTURER)
    
    def get_teachings(self):
        self.get_engagements()

    def add_teaching(self, course):
        self.add_engagement(course)

    def add_teachings(self, courses):
        self.add_engagements(courses)