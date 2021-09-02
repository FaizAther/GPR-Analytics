from __future__ import annotations

from typing import TYPE_CHECKING

from User import User
from UserType import UserType

if TYPE_CHECKING:
    from Course import Course


class Lecturer(User):

    def __init__(self, id: int, type: UserType=UserType.LECTURER):
        super().__init__(id, type)

    def add_engagement(self, engagement) -> None:
        return super().add_engagement(engagement)

    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        super().update(course)
    
    def __whitetest__(self, results) -> bool:
        return super().__whitetest__(results=results)