from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Base import Base
from Instution.Universities.Course import Course

if TYPE_CHECKING:
    from typing import List, Dict
    from Instution.Universities.Course import Course
    from Instution.Events.Location import Location
    from Instution.Users.Lecturer import Lecturer
    from Instution.Users.User import User
'''
    Faculty class
'''
class Faculty(Base):

    def __init__(self, id: int, name=None, description=None):
        super().__init__(id, name, description=description)

        self._count       :int              = 0

        self._courses   :Dict[int, Course]  = {}
        self._locations :List[Location]     = []

    def find_course(self, course):
        return Base.dict_find(course, self.get_courses())

    def add_user(self, user:User, course_id:int, course=None) -> None:
        if course == None:
            course = self.get_courses().get(course_id)
        if (course == None):
            return
        course.add_user(user)

    def add_users(self, users:List[User], course_id:int) -> None:
        course = self.get_courses().get(course_id)
        Base.__DO_SOMETHINGS__(
            lambda u: self.add_user(u, course_id, course=course),
            users
        )

    def make_course_annon(self) -> Course:
        course_id = self._count
        add_course = None
        for offset in range(0,20):
            course = self.get_courses().get(course_id + offset)
            if course == None:
                add_course = self.make_course(course_id + offset)
                break
        return add_course

    def make_course(self, id:int=None, name=None, description=None) -> Course:
        identifier = f"{self.get_name()}-{id}" if name == None else name
        if id == None:
            id = int(name.split('-')[1])
        course = Course(id, name=f"{identifier}", description=description)
        self.add_course(course)
        self._count += 1
        return course

    def get_locations(self) -> List[Location]:
        return self._locations

    def add_location(self, location:Location) -> None:
        Base.ADD_THING_TO(location, self.get_locations())

    def add_locations(self, locations:List[Location]) -> None:
        Base.ADD_THINGS_TO(locations, self.get_locations())

    def get_courses(self) -> Dict[Course]:
        return self._courses

    def get_courses_list(self) -> List[Course]:
        return self._courses.values()

    def add_course(self, course:Course) -> None:
        Base.dict_insert(course, self.get_courses())

    def add_courses(self, courses:List[Course]) -> None:
        Base.__DO_SOMETHINGS__(
            lambda c: self.add_course(c),
            courses
        )

    def insert(self) -> str:
        return super().insert()


    def __repr__(self) -> str:
        courses_str = Base.__LIST_STR__(
            list(self.get_courses_list()), ", courses=")
        return f"{super().__repr__()}, description={self.get_description()}" + \
            f"{courses_str}"

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)

    def generate_html(self) -> str:
        return super().generate_html()