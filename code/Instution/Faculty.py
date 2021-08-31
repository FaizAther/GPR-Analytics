from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from typing import List
    from Course import Course
    from Location import Location

'''
    Faculty class
'''
class Faculty(Base):
    def __init__(self, id: int):
        super().__init__(id)
        self._courses   :List[Course]   = []
        self._locations :List[Location] = []

    def get_locations(self) -> List[Location]:
        return self._locations

    def add_location(self, location:Location) -> None:
        Base.ADD_THING_TO(location, self.get_locations())

    def add_locations(self, locations:List[Location]) -> None:
        Base.ADD_THINGS_TO(locations, self.get_locations())

    def get_courses(self) -> List[Course]:
        return self._courses

    def add_course(self, course:Course) -> None:
        Base.ADD_THING_TO(course, self.get_courses())

    def add_courses(self, courses:List[Course]) -> None:
        Base.ADD_THINGS_TO(courses, self.get_courses())
