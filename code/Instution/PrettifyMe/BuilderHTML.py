from multipledispatch import dispatch
from Instution.Events.Attendance import Attendance
from Instution.Events.Mark import Mark
from Instution.Universities.Course import Course
from Instution.Universities.Faculty import Faculty
from Instution.Universities.University import University
from Instution.Users.Lecturer import Lecturer
from Instution.Users.Student import Student
from Instution.Users.Tutor import Tutor

class BuilderHTML():

    # Users

    @dispatch(Student)
    def generate(concrete: Student):
        pass

    @dispatch(Lecturer)
    def generate(concrete: Lecturer):
        pass

    @dispatch(Tutor)
    def generate(concrete: Tutor):
        pass

    # Universities

    @dispatch(University)
    def generate(concrete: University):
        pass

    @dispatch(Faculty)
    def generate(concrete: Faculty):
        pass

    @dispatch(Course)
    def generate(concrete: Course):
        pass

    # Events

    @dispatch(Attendance)
    def generate(concrete: Attendance):
        pass

    @dispatch(Mark)
    def generate(concrete: Mark):
        pass
