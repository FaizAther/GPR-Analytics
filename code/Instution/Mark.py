from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Attendance import Attendance

if TYPE_CHECKING:
    from typing import Dict, List
    from Tutor import Tutor

'''
    Mark Class
'''
class Mark(Attendance):
    def __init__(self, attendee, marker=None):
        super().__init__(self, attendee, marker)

        self._acheived      :int        = 0
        self._submission    :Dict[datetime, List] \
                                        = 0

        self._deadline      :datetime   = 0
        self._penalty       :int        = 0

    def handle_user(self, user: Tutor):
        user.set_capacity(user.get_capacity() - 1)
        if (user.get_capacity() <= 0):
            self.get_event().move_organizer(self)