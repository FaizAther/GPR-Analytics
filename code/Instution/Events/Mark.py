from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Instution.Events.Attendance import Attendance
from Instution.Users.UserType import UserType

if TYPE_CHECKING:
    from typing import Dict, List
    from Instution.Users.Tutor import Tutor
    from Instution.Users.User import User

'''
    Mark Class
'''
class Mark(Attendance):
    def __init__(self, id, event, attendee, weighting, marker=None, course=None, deadline=None, name=None):
        super().__init__(id, event, attendee, marker=marker, course=course, name=name)

        self._acheived      :int        = 0
        self._submission    :Dict[datetime, List] \
                                        = 0

        self._deadline      :datetime   = deadline
        self._penalty       :int        = 0
        self._weighting     :int        = weighting
        
        self.set_marked()

    def add_user(self, user: User) -> None:
        super().add_user(user)
        self.handle_user(user)

    def get_achieved(self):
        return self._acheived

    def set_achieved(self, acheived):
        self._acheived = acheived

    def get_deadline(self):
        return self._deadline

    def set_deadline(self, deadline):
        self._deadline = deadline

    def handle_user(self, user: User) -> None:
        if (user.get_type() == UserType.TUTOR):
            user.student_assigned()
            if (not user.capacity_available()):
                self.get_event().move_organizer(user)

    def __repr__(self) -> str:
        return super().__repr__()

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)

    def generate_html(self) -> str:
        return super().generate_html()

    def insert(self) -> str:
        return super().insert()