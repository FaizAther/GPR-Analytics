from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
import typing

from Instution.Base import Base
from Instution.Events.Attendance import Attendance
from Instution.Events.EventType import EventType
from Instution.Users.UserType import UserType
from Instution.Events.Mark import Mark

if TYPE_CHECKING:
    from typing import Dict, List

    from Instution.Events.Location import Location
    from Instution.Events.Mark import Mark
    from Instution.Users.User import User
    from Instution.Users.Student import Student
    from Instution.Users.Tutor import Tutor
    from Instution.Users.Lecturer import Lecturer

'''
    Event Class
'''
class Event(Base):

    def __init__(self, id, name=None, type=EventType.DEFAULT):
        super().__init__(id, name=name)

        self._manager       :User               = None
        self._organizers    :List[User]         = []
        self._invitees      :List[Attendance]   = []
        self._guests        :List[User]         = []

        self._start_end     :Dict               = {datetime.now : datetime.now}
        self._weighting     :int                = 0

        self._locations     :List[Location]     = []
        self._type          :EventType          = type
        self._resources     :List               = []

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def set_weighting(self, weighting):
        if weighting >= 0:
            self._weighting = weighting

    def move_organizer(self, user: Tutor):
        self.get_organizers().remove(user)
        self.get_guests().append(user)

    def get_invitees(self) -> List[Attendance]:
        return self._invitees

    def get_organizers(self) -> List[User]:
        return self._organizers

    def get_guests(self) -> List[User]:
        return self._guests

    def get_weighting(self) -> int:
        return self._weighting

    def add_user(self, user: User) -> None:
        if user.get_type() == UserType.TUTOR:
            self.handle_tutor(user),
        elif user.get_type() == UserType.LECTURER:
            self.handle_lecturer(user)
        else:
            self.handle_student(user)

    def add_users(self, users: List[User]):
        Base.__DO_SOMETHINGS__(lambda u: self.add_user(u), users)

    def find_marker(self):
        return Base.FOLDL(lambda z, m: \
                m if z == None and m.get_type() == UserType.TUTOR \
                    and m.capacity_available() \
                else z, None, self.get_organizers())

    def handle_student(self, user: Student) -> None:
        marker = self.find_marker()
        if (self.get_weighting() <= 0):
            attendance = Attendance(0, self, user, marker=marker)
        else:
            attendance = Mark(0, self, user, self.get_weighting(), marker=marker)

        Base.ADD_THING_TO(attendance, self.get_invitees())

    def handle_tutor(self, user: Tutor) -> None:
        if user.capacity_available():
            Base.ADD_THING_TO(user, self.get_organizers())
        else:
            Base.ADD_THING_TO(user, self.get_guests())

    def handle_lecturer(self, user: Lecturer) -> None:
        if self._manager == None:
            self._manager = user
        else:
            self.get_guests().append(user)

    def __repr__(self) -> str:
        return super().__repr__()

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)

    def generate_html(self) -> str:
        return super().generate_html()

    def insert(self) -> str:
        return super().insert()