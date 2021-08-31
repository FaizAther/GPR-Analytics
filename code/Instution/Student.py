from __future__ import annotations

from typing import TYPE_CHECKING

from User import User
from UserType import UserType

if TYPE_CHECKING:
    from Course import Course


class Student(User):
    
    DEFAULT_TEST = [
        f"Student('id=0, name=0, type=UNDERGRAD, engagements=')",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=')",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=\n----\nsmith\n----\n')",
        "N.A.",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')",
        UserType.UNDERGRAD
    ]
    
    def __init__(self, id: int, type: UserType=UserType.UNDERGRAD):
        super().__init__(id, type)
    
    def generate_html(self):
        return ""
    
    def update(self, course: Course):
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
