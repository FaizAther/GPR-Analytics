from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from typing import List

    from Event import Event
    from User import User

'''
    Course class
'''
class Course(Base):
    
    def __init__(self, id: int, admin: User=None):
        super().__init__(id)
        self._admin     :User        = admin
        self._users     :List[User]  = []
        self._events    :List[Event] = []

    def get_events(self) -> List[Event]:
        return self._events
    
    def add_event(self, event: Event) -> None:
        Base.ADD_THING_TO(event, self.get_events())
    
    def add_events(self, events: List[Event]) -> None:
        Base.ADD_THINGS_TO(events, self.get_events())
    
    def get_users(self) -> List[User]:
        return self._users

    def add_user(self, user: User) -> None:
        Base.ADD_THING_TO(user, self.get_users())
        Base.ADD_THING_TO(self, user.get_engagements())

    def add_users(self, users: List[User]) -> None:
        Base.__DO_SOMETHINGS__(lambda u:self.add_user(u), users)
    
    def notify(self) -> None:
        Base.__DO_SOMETHINGS__(lambda x: x.update(self), self.get_users())
        
    def generate_html(self) -> str:
        return ""
    
    def __repr__(self) -> str:
        return super().__repr__()

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)