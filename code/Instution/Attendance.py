from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from Course import Course
    from User import User

'''
    Mark Class
'''
class Attendance(Base):
    def __init__(self):
        super().__init__(self)
        
        self._attandee  :User   = None
        self._marker    :User   = None

        self._attended  :bool   = False
        self._duration  :int    = 0