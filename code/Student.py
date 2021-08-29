from User import User
'''
    Student Class
'''
class Student(User):
    def __init__(self, id, type):
        super().__init__(id)
        self._type = type

    def get_courses(self):
        self.get_engagements()

    def add_course(self, course):
        self.add_engagement(course)

    def add_courses(self, courses):
        self.add_engagements(courses)