from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Base import Base
from Attendance import Attendance

if TYPE_CHECKING:
    from typing import Dict, List

    from EventType import EventType
    from Location import Location
    from Mark import Mark
    from User import User
    from Student import Student
    from Tutor import Tutor
    from Lecturer import Lecturer

'''
    Event Class
'''
class Event(Base):
    def __init__(self, id, type=EventType.DEFAULT):
        super().__init__(id)

        self._manager       :User               = None
        self._organizers    :List[User]         = []
        self._invitees      :List[Attendance]   = []
        self._guests        :List[User]         = []

        self._start_end     :Dict               = {datetime.now : datetime.now}
        self._weighting     :int                = 0

        self._locations     :List[Location]     = []
        self._type          :EventType          = type
        self._resources     :List               = []
    
    def get_invitees(self) -> List[Attendance]:
        return self._invitees

    def get_organizers(self) -> List[User]:
        return self._organizers

    def get_weighting(self) -> int:
        return self._weighting
    
    def add_user(self, user: User) -> None:
        self.handle_user(user)

    def handle_user(self, user: Student) -> None:
        if (self.get_weighting() <= 0):
            attendance = Attendance(user)
        else:
            attendance = Mark(user)

        Base.ADD_THING_TO(attendance, self.get_invitees())

    def handle_user(self, user: Tutor) -> None:
        Base.ADD_THING_TO(user, self.get_organizers())

    def handle_user(self, user: Lecturer) -> None:
        if self._manager == None:
            self._manager = user