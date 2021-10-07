from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Users.User import User
from Instution.Users.UserType import UserType

if TYPE_CHECKING:
    from Instution.Universities.Course import Course


class Student(User):

    def __init__(self, id: int, type: UserType=UserType.UNDERGRAD):
        super().__init__(id, type)

    def add_engagement(self, engagement) -> None:
        super().add_engagement(engagement)

    def generate_html(self):
        return ""

    def update(self, course: Course):
        super().update(course)
        #print(course)
    
    def insert(self) -> str:
        return super().insert()

    def __whitetest__(self, results) -> bool:
        return super().__whitetest__(results=results)