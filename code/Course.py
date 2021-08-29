from IdClass import IdClass
'''
    Course class
'''
class Course(IdClass):
    def __init__(self, id):
        super().__init__(id)
        self._lecturers = []
        self._tutors    = []
        self._students  = []
        self._events    = []
