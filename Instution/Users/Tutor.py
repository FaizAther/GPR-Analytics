from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Users.User import User
from Instution.Users.UserType import UserType

if TYPE_CHECKING:
    from Instution.Universities.Course import Course


class Tutor(User):

    def __init__(self, id: int, type: UserType=UserType.TUTOR, capacity:int=3, name=None, description=None):
        super().__init__(id, typename=name, description=description)
        self._capacity = capacity

    def capacity_available(self):
        return self._capacity > 0

    def student_assigned(self):
        self._capacity -= 1

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)

    def get_capacity(self) -> int:
        return self._capacity

    def set_capacity(self, capacity) -> None:
        self._capacity = capacity

    def generate_html(self):
        return ""

    def update(self, course: Course):
        super().update(course)
    
    def insert(self) -> str:
        return super().insert()

    def __whitetest__(self, results) -> bool:
        return super().__whitetest__(results=results)