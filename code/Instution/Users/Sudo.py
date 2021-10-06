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
        self.get_admins().append(Admin(len(self._admins)))

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)
    
    def generate_html(self):
        return super().generate_html()
    
    def update(self, subject):
        return super().update(subject)
    
    def insert(self):
        pass

my_sudo = Sudo(5, 5)
print(my_sudo)
