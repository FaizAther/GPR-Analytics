from Base       import Base
from Course     import Course
from Location   import Location
'''
    Faculty class
'''
class Faculty(Base):
    def __init__(self, id: int):
        super().__init__(id)
        self._courses   :list[Course] = list[Course]
        self._locations :list[Location] = list[Location]