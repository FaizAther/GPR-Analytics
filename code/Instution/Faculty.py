from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base
from Course import Course

if TYPE_CHECKING:
    from typing import List, Dict
    from Course import Course
    from Location import Location
    from Lecturer import Lecturer
    from User import User
'''
    Faculty class
'''
class Faculty(Base):

    def __init__(self, id: int, name=None):
        super().__init__(id, name)

        self._count       :int              = 0

        self._courses   :Dict[int, Course]  = {}
        self._locations :List[Location]     = []

    def find_course(self, course_id: int) -> Course:
        return self.get_courses().get(course_id + Base.__ID__OFFSET__)

    def add_user(self, user:User, course_id:int, course=None) -> None:
        if course == None:
            course = self.find_course(course_id)

        course.add_user(user)

    def add_users(self, users:List[User], course_id:int) -> None:
        course = self.find_course(course_id)
        Base.__DO_SOMETHINGS__(
            lambda u: self.add_user(u, course_id, course=course),
            users)

    def make_course(self, id:int) -> None:
        self.add_course(Course(id, name=f"{self.get_name()}-{id}"))
        self._count += 1

    def get_locations(self) -> List[Location]:
        return self._locations

    def add_location(self, location:Location) -> None:
        Base.ADD_THING_TO(location, self.get_locations())

    def add_locations(self, locations:List[Location]) -> None:
        Base.ADD_THINGS_TO(locations, self.get_locations())

    def get_courses(self) -> List[Course]:
        return self._courses

    def add_course(self, course:Course) -> None:
        if self.find_course(course.get_id()) == None:
            self.get_courses()[course.get_id()] = course

    def add_courses(self, courses:List[Course]) -> None:
        Base.__DO_SOMETHINGS__(
            lambda c: self.add_course(c),
            self.get_courses()
        )
    
    def __repr__(self) -> str:
        return super().__repr__()
    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)
    def generate_html(self) -> str:
        return super().generate_html()
