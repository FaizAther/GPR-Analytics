from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from Course import Course
    from User import User
    from Student import Student
    from Tutor import Tutor
    from Event import Event

'''
    Mark Class
'''
class Attendance(Base):

    def __init__(self, id, event, attendee, marker=None):
        super().__init__(id)

        self._attandee  :User   = attendee
        self._marker    :User   = marker

        self._attended  :bool   = False
        self._duration  :int    = 0

        self._event     :Event  = event

        for user in [attendee, marker]:
            if user != None:
                self.add_user(user)

    def get_marker(self):
        return self._marker

    def get_event(self) -> Event:
        return self._event

    def add_user(self, user: User) -> None:
        user.add_engagement(self)