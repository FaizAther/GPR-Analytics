from __future__ import annotations

from typing import TYPE_CHECKING

from abc import abstractmethod
from Base import Base
from UserType import UserType

if TYPE_CHECKING:
    from typing import List

'''
    User class
'''
class User(Base):
    
    DEFAULT_PASSWORD    :str    = "password"

    def HASH_HEX_DIGEST(value: str) -> str:
        import hashlib
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def __init__(self, id: int, type: UserType):
        super().__init__(id)
        self._engagements   :List       = []
        self._password      :str        = ""
        self._type          :UserType   = type
        self.set_password(User.DEFAULT_PASSWORD)
    
    @abstractmethod
    def generate_html(self):
        pass
    
    @abstractmethod
    def update(self, subject):
        pass

    def get_type(self) -> UserType:
        return self._type

    def validate_password(self, password: str) -> bool:
        return self._password == User.HASH_HEX_DIGEST(password)

    def set_password(self, password: str) -> None:
        self._password = User.HASH_HEX_DIGEST(password)

    def get_engagements(self) -> List:
        return self._engagements

    def add_engagement(self, engagement) -> None:
        Base.add_something(engagement, self.get_engagements())

    def add_engagements(self, engagements) -> None:
        Base.add_somethings(engagements, self.get_engagements())

    def __repr__(self) -> str:
        return f"{self.get_type().name}('{self.__str__()}')"

    def __str__(self) -> str:
        engagements_str = Base.__LIST_STR__(
            self.get_engagements(), ", engagements=")    
        return super().__str__() + engagements_str

    @abstractmethod
    def __whitetest__(self, results) -> bool:
        return True
    
    DEFAULT_TEST = [
        f"UNDERGRAD('id=0, name=0, engagements=')",
        f"UNDERGRAD('id=0, name=john, engagements=')",
        f"UNDERGRAD('id=0, name=john, engagements=\n----\nsmith\n----\n')",
        "",
        f"UNDERGRAD('id=0, name=john, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')",
        UserType.UNDERGRAD
    ]

