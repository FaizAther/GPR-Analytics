from __future__ import annotations

from typing import TYPE_CHECKING

from User import User
from UserType import UserType
from Mark import Mark

if TYPE_CHECKING:
    from Course import Course


class Tutor(User):
    
    def __init__(self, id: int, type: UserType=UserType.TUTOR, capacity:int=3):
        super().__init__(id, type)
        self._capacity = capacity

    def add_engagement(self, engagement) -> None:
        if (isinstance(engagement, Mark)):
            self.set_capacity(self.get_capacity() - 1)
            if (self.get_capacity() == 0):
                engagement.get_event().move_organizer(self)
        return super().add_engagement(engagement)
    
    def get_capacity(self) -> int:
        return self._capacity
    
    def set_capacity(self, capacity) -> None:
        self._capacity = capacity
    
    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        super().update(course)
        print(self)
        print(course)
    
    def __whitetest__(self, results) -> bool:
        return super().__whitetest__(results=results)