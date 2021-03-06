from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Base import Base

if TYPE_CHECKING:
    from Instution.Universities.Course import Course
    from Instution.Users.User import User
    from Instution.Users.Student import Student
    from Instution.Users.Tutor import Tutor
    from Instution.Events.Event import Event

'''
    Mark Class
'''
class Attendance(Base):

    def __init__(self, id, event, attendee, marker=None, course=None, name=None):
        id = len(attendee.get_engagements())
        super().__init__(id, name=name)

        self._attandee  :User   = attendee
        self._marker    :User   = marker

        self._attended  :bool   = False
        self._duration  :int    = 0

        self._event     :Event  = event
        self._course    :Course = course
        self._marked            = False

        for user in [attendee, marker]:
            if user != None:
                self.add_user(user)
        
        if marker == None and course != None and course.get_admin() != None:
            # print(course.get_admin())
            course.get_admin().add_markings(self)

    def get_attendee(self):
        return self._attandee

    def set_marked(self):
        self._marked = not self._marked

    def is_marked(self):
        return self._marked

    def get_course(self):
        return self._course

    def get_marker(self):
        return self._marker

    def get_event(self) -> Event:
        return self._event

    def add_user(self, user: User) -> None:
        user.add_engagement(self)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def __whitetest__(self, result=...) -> bool:
        return super().__whitetest__(result=result)
    
    def generate_html(self) -> str:
        return super().generate_html()
    
    def insert(self) -> str:
        return super().insert()