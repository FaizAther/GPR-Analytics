from Base import Base
'''
    Course class
'''
class Course(Base):
    def __init__(self, id):
        super().__init__(id)
        self._lecturers = []
        self._tutors    = []
        self._students  = []
        self._events    = []
