from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Users.User import User
from Instution.Users.UserType import UserType

if TYPE_CHECKING:
    from Instution.Universities.Course import Course


class Lecturer(User):

    def __init__(self, id: int, type: UserType=UserType.LECTURER, name=None, description=None):
        super().__init__(id, type, name=name, description=description)

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)

    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        super().update(course)
    
    def insert(self) -> str:
        return super().insert()

    def __whitetest__(self, results) -> bool:
        return super().__whitetest__(results=results)