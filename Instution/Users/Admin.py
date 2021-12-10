from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Users.User import User
from Instution.Users.UserType import UserType
from Instution.Universities.University import University

if TYPE_CHECKING:
    # from Instution.Universities.Course import Course
    pass

class Admin(User):

    def __init__(self, id, name=None, description=None, type=UserType.ADMIN):
        super().__init__(id, type, name=name)
        self._university = University(id, admin=self, name=name, description=description)

    def get_university(self) -> University:
        return self._university

    def get_functions(self):
        return [(0, "Faculty"), (1, "User"), (3, "Course")]
    
    def commit(self, action: int, name=None, type_select=UserType.DEFAULT):
        if action == 0:
            self._university.make_faculty(name=name)
        elif action == 1:
            self._university.make_user(list(UserType)[int(type_select)], name=name)
        elif action == 2:
            try:
                fac = self._university.find_faculty(name.split('-')[0])
                # print(fac, "FUCL")
                fac.make_course(0, name=name.split('-')[1])
            except:
                pass

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)
    
    def generate_html(self):
        return super().generate_html()
    
    def update(self, subject):
        return super().update(subject)

    def insert(self):
        pass