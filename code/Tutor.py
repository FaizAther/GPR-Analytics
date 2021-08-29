from StaffType import StaffType
from User import User
from Staff import Staff
'''
    Lecturer Class
'''

class Lecturer(Staff):
    def __init__(self):
        super().__init__(self, StaffType.TUTOR)
    
    def get_tutoring(self):
        self.get_engagements()

    def add_tutoring(self, course):
        self.add_engagement(course)

    def add_tutorings(self, courses):
        self.add_engagements(courses)