from Base           import Base
from LocationType   import LocationType
'''
    Location Class
'''
class Location(Base):
    def __init__(self, type: LocationType, page: str, address: str):
        super.__init__(self)
        self._type    :LocationType = type
        self._page    :str          = page
        self._address :str          = address
