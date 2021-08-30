from Base       import Base
from User       import User
from Location   import Location
from EventType  import EventType
from datetime   import datetime
from typing     import List, Dict
'''
    Event Class
'''
class Event(Base):
    def __init__(self, id, type):
        super().__init__(id)
        self._date_duration :Dict           = {datetime.now : 0}
        self._manager       :User           = None
        self._organizers    :List[User]     = []
        self._guests        :List[User]     = []
        self._invitees      :List[User]     = []
        self._attendance    :List[User]     = []
        self._locations     :List[Location] = []
        self._resources     :List           = []
        self._type          :EventType      = type