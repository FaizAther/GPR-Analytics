from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
import typing

from Instution.Base import Base
from Instution.Events.Attendance import Attendance
from Instution.Events.EventType import EventType
from Instution.Users.UserType import UserType
from Instution.Events.Mark import Mark
from Instution.Items.Resource import Resource

if TYPE_CHECKING:
    from typing import Dict, List

    from Instution.Events.Location import Location
    from Instution.Events.Mark import Mark
    from Instution.Users.User import User
    from Instution.Users.Student import Student
    from Instution.Users.Tutor import Tutor
    from Instution.Users.Lecturer import Lecturer
    from Instution.Universities.Course import Course


'''
    Event Class
'''
class Event(Base):

    def __init__(self, id, start_date, end_date, name=None, description=None, creation=None, \
        type=EventType.DEFAULT, filename=None):
        super().__init__(id, name=name, description=description)

        self._manager       :User               = None
        self._organizers    :List[User]         = []
        self._invitees      :List[Attendance]   = []
        self._guests        :List[User]         = []

        self._start_end     :Dict               = {}
        self._weighting     :int                = 0

        self._locations     :List[Location]     = []
        self._type          :EventType          = type
        self._resources     :List               = filename
        self._creation                          = creation if creation != None else datetime.now
        self._start_date = start_date if start_date != None else datetime.now
        self._end_date = end_date if end_date != None else datetime.now

    def get_resources(self):
        return self._resources
    
    # def make_resource(self, filename):
    #     self._resources.append(Resource(data=filename))

    def get_start_end(self):
        return self._start_end
    
    def set_start_end(self, start_end):
        self._start_end = start_end

    def get_end_date(self):
        return self._end_date

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

    # contains tutors/guest lecturers - not lecturer themselves
    def get_organizers(self) -> List[User]:
        return self._organizers

    def get_guests(self) -> List[User]:
        return self._guests

    def get_weighting(self) -> int:
        return self._weighting

    def add_user(self, user: User, course: Course, deadline=None, name=None) -> None:
        if user.get_type() == UserType.TUTOR:
            self.handle_tutor(user),
        elif user.get_type() == UserType.LECTURER:
            self.handle_lecturer(user)
        else:
            self.handle_student(user, course, deadline, name=name)

    def add_users(self, users: List[User], course, deadline=None, name=None):
        Base.__DO_SOMETHINGS__(lambda u: self.add_user(u, course, deadline=deadline, name=name), users)

    def find_marker(self):
        return Base.FOLDL(lambda z, m: \
                m if z == None and m.get_type() == UserType.TUTOR \
                    and m.capacity_available() \
                else z, None, self.get_organizers())

    def get_manager(self):
        return self._manager

    def handle_student(self, user: Student, course: Course, deadline=None, name=None) -> None:
        marker = self.find_marker()
        marker = self.get_manager() if marker == None else marker
        # print(user)
        id = 0
        if (self.get_weighting() <= 0):
            attendance = Attendance(id, self, user, marker=marker, course=course, name=name)
        else:
            attendance = Mark(id, self, user, self.get_weighting(), marker=marker, course=course, deadline=deadline, name=name)

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