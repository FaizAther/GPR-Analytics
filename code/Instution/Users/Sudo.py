from __future__ import annotations

from typing import TYPE_CHECKING, List

from Instution.Users.User import User
from Instution.Users.UserType import UserType
from Instution.Users.Admin import Admin

if TYPE_CHECKING:
    pass

class Sudo(User):

    def __init__(self, id, type=UserType.SUDO):
        super().__init__(id, type)
        self._admins: List[Admin] = []

    def get_admins(self) -> List[Admin]:
        return self._admins

    def add_admin(self):
        admin = Admin(len(self._admins))
        self.get_admins().append(admin)
        return admin

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

