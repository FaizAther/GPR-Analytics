from _typeshed import NoneType
from Base import Base
'''
    Mark Class
'''
class Mark(Base):
    def __init__(self):
        super().__init__(self)
        self._weighting = 0
        self._total     = 0
        self._acheived  = 0
        self._attended  = False
        self._course    = None
        self._student   = None
        self._marker    = None