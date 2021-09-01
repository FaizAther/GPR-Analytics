from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Attendance import Attendance
from UserType import UserType

if TYPE_CHECKING:
    from typing import Dict, List
    from Tutor import Tutor
    from User import User

'''
    Mark Class
'''
class Mark(Attendance):
    def __init__(self, id, event, attendee, weighting, marker=None):
        super().__init__(id, event, attendee, marker=marker)

        self._acheived      :int        = 0
        self._submission    :Dict[datetime, List] \
                                        = 0

        self._deadline      :datetime   = 0
        self._penalty       :int        = 0
        self._weighting     :int        = weighting


    def add_user(self, user: User) -> None:
        user.add_engagement(self)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def __whitetest__(self, result) -> bool:
        return super().__whitetest__(result=result)
    
    def generate_html(self) -> str:
        return super().generate_html()