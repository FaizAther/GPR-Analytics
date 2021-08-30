from User import User
from EventType import EventType
from Base import Base
from datetime import datetime
'''
    Event Class
'''
class Event(Base):
    def __init__(self, id, type):
        super().__init__(id)
        self._date_duration :dict       = {datetime.now : 0}
        self._manager       :User       = None
        self._organizers    :list[User] = list[User]
        self._guests        :list[User] = list[User]
        self._invitees      :list[User] = list[User]
        self._attendance    :list[User] = list[User]
        self._locations     :list[User] = list[User]
        self._resources     :list[User] = list[User]
        self._type          :EventType  = type