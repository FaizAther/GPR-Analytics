from StaffType import StaffType
from User import User
from Staff import Staff
'''
    Lecturer Class
'''

class Lecturer(Staff):
    def __init__(self):
        super().__init__(self, StaffType.RESEARCHER)
    
    def get_projects(self):
        self.get_engagements()

    def add_project(self, course):
        self.add_engagement(course)

    def add_projects(self, courses):
        self.add_engagements(courses)