from Base import Base
'''
    Location Class
'''
class Location(Base):
    def __init__(self, type, page, address):
        super.__init__(self)
        self._type      = type
        self._page      = page
        self._address   = address
