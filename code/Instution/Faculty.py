from Base       import Base
from Course     import Course
from Location   import Location
from typing     import List
'''
    Faculty class
'''
class Faculty(Base):
    def __init__(self, id: int):
        super().__init__(id)
        self._courses   :List[Course]   = []
        self._locations :List[Location] = []