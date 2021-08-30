from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from typing import List
    from Course import Course
    from Location import Location

'''
    Faculty class
'''
class Faculty(Base):
    def __init__(self, id: int):
        super().__init__(id)
        self._courses   :List[Course]   = []
        self._locations :List[Location] = []
