from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base
from UserType import UserType

if TYPE_CHECKING:
    from typing import List

    from Event import Event
    from User import User
    from Student import Student
    from Tutor import Tutor
    from Lecturer import Lecturer
'''
    Course class
'''
class Course(Base):
    
    def __init__(self, id: int, admin: User=None, name=None):
        super().__init__(id, name)
        self._admin     :User        = admin
        self._users     :List[User]  = []
        self._events    :List[Event] = []

    def get_events(self) -> List[Event]:
        return self._events
    
    def add_event(self, event: Event) -> None:
        Base.ADD_THING_TO(event, self.get_events())
    
    def add_events(self, events: List[Event]) -> None:
        Base.__DO_SOMETHINGS__(lambda e: self.add_event(e), events)
    
    def get_users(self) -> List[User]:
        return self._users

    def add_user(self, user: User) -> None:
        Base.ADD_THING_TO(user, self.get_users())
        Base.ADD_THING_TO(self, user.get_engagements())
        if user.get_type() == UserType.LECTURER:
            self.handle_lecturer(user)

    def handle_user(self, user: Student) -> None:
        pass

    def handle_user(self, user: Tutor) -> None:
        pass

    def handle_lecturer(self, user: Lecturer) -> None:
        if self._admin == None:
            self._admin = user

    def add_users(self, users: List[User]) -> None:
        Base.__DO_SOMETHINGS__(lambda u:self.add_user(u), users)
    
    def notify(self) -> None:
        Base.__DO_SOMETHINGS__(lambda x: x.update(self), self.get_users())
        
    def generate_html(self) -> str:
        return ""
    
    def get_admin(self) -> Lecturer:
        return self._admin

    def __repr__(self) -> str:
        return super().__repr__()

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)