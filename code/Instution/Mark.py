from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from Course import Course
    from User import User

'''
    Mark Class
'''
class Mark(Base):
    def __init__(self):
        super().__init__(self)
        self._weighting :int    = 0
        self._total     :int    = 0
        self._acheived  :int    = 0
        self._attended  :bool   = False
        self._course    :Course = None
        self._student   :User   = None
        self._marker    :User   = None
