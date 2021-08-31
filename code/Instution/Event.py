from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Base import Base
from Attendance import Attendance
from EventType import EventType

if TYPE_CHECKING:
    from typing import Dict, List

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
        self.handle_user(user)
    
    def add_users(self, users: List[User]):
        Base.__DO_SOMETHINGS__(lambda u: self.add_user(u), users)

    def find_marker(self):
        Base.FOLDL(lambda z, m: \
            m if m.get_capacity() > 0 \
            else z, None, self.get_organizers())

    def handle_user(self, user: Student) -> None:
        marker = self.find_marker()
        if (self.get_weighting() <= 0):
            attendance = Attendance(self, user, marker)
        else:
            attendance = Mark(self, user, marker)

        Base.ADD_THING_TO(attendance, self.get_invitees())

    def handle_user(self, user: Tutor) -> None:
        if user.get_capacity() > 0:
            Base.ADD_THING_TO(user, self.get_organizers())
        Base.ADD_THING_TO(user, self.get_guests())

    def handle_user(self, user: Lecturer) -> None:
        if self._manager == None:
            self._manager = user
        
    def __repr__(self) -> str:
        return super().__repr__()
    
    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)
    
    def generate_html(self) -> str:
        return super().generate_html()