from __future__ import annotations

from typing import TYPE_CHECKING

from User import User
from UserType import UserType

if TYPE_CHECKING:
    from Course import Course


class Lecturer(User):
    
    DEFAULT_TEST = [
        f"Lecturer('id=0, name=0, type=LECTURER, engagements=')",
        f"Lecturer('id=0, name=john, type=LECTURER, engagements=')",
        f"Lecturer('id=0, name=john, type=LECTURER, engagements=\n----\nsmith\n----\n')",
        "N.A.",
        f"Lecturer('id=0, name=john, type=LECTURER, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')",
        UserType.LECTURER
    ]

    def __init__(self, id: int, type: UserType=UserType.LECTURER):
        super().__init__(id, type)

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)

    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        super().update(course)
        print(self)
        print(course)
    
    def __whitetest__(self, results=DEFAULT_TEST) -> bool:
        assert(self.__str__() == results[0])
        self.set_name("john")
        assert(self.__str__() == results[1])
        self.add_engagement("smith")
        assert(self.__str__() == results[2])
        assert(self.get_html() == results[3])
        self.add_engagements(["doe", "jack"])
        assert(self.__str__() == results[4])
        assert(self.get_type() == results[5])
        assert(self.validate_password(User.DEFAULT_PASSWORD))
        return True
