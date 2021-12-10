from __future__ import annotations
from threading import get_ident

from typing import TYPE_CHECKING, Dict, List

from Instution.Users.User import User
from Instution.Users.UserType import UserType
from Instution.Users.Admin import Admin

if TYPE_CHECKING:
    from Instution.Universities.University import University

class Sudo(User):

    def __init__(self):
        super().__init__(0, type=UserType.SUDO)
        self._admins: Dict[Admin] = {}
        self._selection = []

    def get_admins(self) -> Dict[Admin]:
        return self._admins

    def find_admin(self, id) -> Admin:
        return self.dict_find(id, self.get_admins())

    def add_admin(self, name=None, description=None):
        admin = Admin(len(self._admins), name=name, description=description)
        self.dict_insert(admin, self.get_admins())
        university = admin.get_university()
        self._selection += [(university.get_id(), university.get_name())]
        return admin

    def get_selection(self):
        return self._selection

    def find_university(self, id: int) -> University:
        admin = self.dict_find(id, self.get_admins())
        return admin.get_university() if admin != None else None

    def find_user(self, university_id: int, user_id: int) -> User:
        return self.find_university(university_id).find_user(user_id)

    def get_universities(self):
        return [admin.get_university() for admin in self.get_admins().values()]

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)
    
    def generate_html(self):
        return super().generate_html()
    
    def update(self, subject):
        return super().update(subject)
    
    def insert(self):
        pass

if __name__ == "__main__":
    print("just test")
    my_sudo = Sudo(5, 5)
    print(my_sudo)
    my_admin = my_sudo.add_admin()
    print(my_admin)
    my_univeristy = my_admin.get_iniversity()
    print(my_univeristy)
    my_faculty = my_univeristy.make_faculty("COMP")
    print(my_faculty)
    course = my_faculty.make_course_annon()
    print(course)
    print(my_faculty)

