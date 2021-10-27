from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Base import Base

from Instution.Users.UserType import UserType
from Instution.Events.EventType import EventType
from Instution.Events.Event import Event
from Instution.Items.Announcement import Announcement
from datetime import datetime

if TYPE_CHECKING:
    from typing import List

    from Instution.Users.User import User
    from Instution.Users.Student import Student
    from Instution.Users.Tutor import Tutor
    from Instution.Users.Lecturer import Lecturer

'''
    Course class
'''
class Course(Base):

    def __init__(self, id: int, admin: User=None, name=None, description=None):
        super().__init__(id, name=name, description=description)
        self._admin     :User        = admin
        self._tutors    :Tutor       = []
        self._users     :List[User]  = []
        self._events    :List[Event] = []
        self._announcements: List[Announcement] = []

    def get_announcements(self):
        return self._announcements

    def make_announcement(self, id, time=None, description=None):
        annon = Announcement(id, time=time, description=description)
        self.add_announcement(annon)
        return annon


    def add_announcements(self, announcements: List[Announcement]) -> None:
        for a in announcements:
            self.add_announcement(a)

    def add_announcement(self, announcement: Announcement) -> None:
        self._announcements.append(announcement)

    def update(self, user):
        if user != self.get_admin():
            return
        event = self.add_event()
        return event

    # {'id': 115, 'course_id': 9, 'position': 2, 'created_date': '2021-10-27 00:45:53.651011',
    # 'description': None, 'name': 'PRACTICAL 1', 'manager_id': 10, 'resource_id': None,
    # 'type': 2, 'start_date': '2021-10-27 00:45:53.651016',
    # 'end_date': '2022-04-25 00:45:53.651018', 'reacurring': 1, 'day_of_week': 0,
    # 'time_of_day': 3, 'marked': 0}
    def make_event(self, id, type, name, \
            start_date, end_date, weighting, \
            reacurring=False, description=None, creation=None, day_of_week=None, time_of_day=None):
        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)
        event = Event(id, start_date, end_date, name=name, description=description, creation=creation, type=EventType(type))
        dates = {}
        if reacurring:
            pass
        else:
            event.set_weighting(weighting)

        event.add_users(self.get_users())
        self.add_event(event)
        return event

    def get_events(self) -> List[Event]:
        return self._events

    def add_event(self, event: Event=None) -> Event:
        if event == None:
            event = Event(len(self.get_events()))
        Base.ADD_THING_TO(event, self.get_events())
        return event

    def add_events(self, events: List[Event]) -> None:
        Base.__DO_SOMETHINGS__(lambda e: self.add_event(e), events)

    def get_users(self) -> List[User]:
        return self._users

    def add_user(self, user: User) -> None:
        Base.ADD_THING_TO(user, self.get_users())
        user.add_engagement(self)
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

    def notify(self, event) -> None:
        Base.__DO_SOMETHINGS__(lambda u: u.update(event), self.get_users())

    def generate_html(self) -> str:
        super().generate_html()

    def get_admin(self) -> Lecturer:
        return self._admin

    def insert(self) -> str:
        return super().insert()

    def __repr__(self) -> str:
        return super().__repr__() + \
            f", admin={self.get_admin().__str__()}"

    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)