from Base import Base
'''
    Faculty class
'''
class Faculty(Base):
    def __init__(self, id):
        super().__init__(id)
        self._courses   = []
        self._locations = []