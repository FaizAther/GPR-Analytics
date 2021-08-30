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

'''
    Event Class
'''
class Event(Base):
    def __init__(self, id, type=EventType.DEFAULT):
        super().__init__(id)

        self._manager       :User               = None
        self._organizers    :List[User]         = []
        self._invitees      :Attendance         = []
        self._guests        :List[User]         = []

        self._start_end     :Dict               = {datetime.now : datetime.now}
        self._weighting     :int                = 0
        self._total         :int                = 0
        
        self._locations     :List[Location]     = []
        self._type          :EventType          = type
        self._resources     :List               = []
