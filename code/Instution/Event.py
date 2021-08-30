from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Base import Base

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
        self._date_duration :Dict               = {datetime.now : datetime.now}
        self._manager       :User               = None
        self._organizers    :List[User]         = []
        self._guests        :List[User]         = []
        self._invitees      :Dict[User, Mark]   = {}
        self._attendance    :List[User]         = []
        self._locations     :List[Location]     = []
        self._resources     :List               = []
        self._type          :EventType          = type
