from multipledispatch import dispatch
from typing import TYPE_CHECKING

from Instution.Universities.University import University
from Instution.Universities.Faculty import Faculty
from Instution.Universities.Course import Course
from Instution.Users.Lecturer import Lecturer
from Instution.Users.Student import Student
from Instution.Users.Tutor import Tutor
from Instution.Events.Mark import Mark
from Instution.Events.Attendance import Attendance

if TYPE_CHECKING:
    pass

class BuilderHTML():

    # Users

    @dispatch(Student)
    def generate(concrete: Student) -> str:
        return '<div>' + concrete.get_name() +'<\div>'

    @dispatch(Lecturer)
    def generate(concrete: Lecturer):
        pass

    @dispatch(Tutor)
    def generate(concrete: Tutor):
        pass

    # Universities

    @dispatch(University)
    def generate(concrete: University):
        facultys_html = ''
        print(concrete.get_faculties_list())
        for faculty in concrete.get_faculties_list():
            facultys_html += BuilderHTML.generate(faculty)
        return '<div><p>' + 'University: ' + concrete.get_name() + ' ID: ' + concrete.get_id().__str__() + facultys_html + '</p></div>'

    @dispatch(Faculty)
    def generate(concrete: Faculty):
        courses_html = ''
        for course in concrete.get_courses_list():
            courses_html += BuilderHTML.generate(course)

        return '<div><p>' + 'Faculty: ' + concrete.get_name() + ' ID: ' + concrete.get_id().__str__() + courses_html +'</p></div>'

    @dispatch(Course)
    def generate(concrete: Course):
        user_len = len(concrete.get_users())
        return '<div><p>' + 'Course: ' + concrete.get_name() + ' ID: ' + concrete.get_id().__str__() + ' Enrollment ' + user_len.__str__() + '</p></div>'

    # Events

    @dispatch(Attendance)
    def generate(concrete: Attendance):
        pass

    @dispatch(Mark)
    def generate(concrete: Mark):
        pass
