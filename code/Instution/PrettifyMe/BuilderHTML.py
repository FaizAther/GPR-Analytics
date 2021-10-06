from multipledispatch import dispatch
from Instution.Universities.Course import Course
from Instution.Universities.Faculty import Faculty
from Instution.Universities.University import University
from Instution.Users.Lecturer import Lecturer
from Instution.Users.Student import Student
from Instution.Users.Tutor import Tutor

class BuilderHTML():

    @dispatch(Student)
    def generate(concrete: object):
        pass

    @dispatch(Lecturer)
    def generate(concrete: object):
        pass

    @dispatch(Tutor)
    def generate(concrete: object):
        pass

    @dispatch(University)
    def generate(concrete: object):
        pass

    @dispatch(Faculty)
    def generate(concrete: object):
        pass

    @dispatch(Course)
    def generate(concrete: object):
        pass
