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
        print(f"uuid={self.get_id()} reacted to\nengagement=\t{subject.__str__()}")

    def get_type(self) -> UserType:
        return self._type

    def validate_password(self, password: str) -> bool:
        return self._password == User.HASH_HEX_DIGEST(password)

    def set_password(self, password: str) -> None:
        self._password = User.HASH_HEX_DIGEST(password)

    def get_engagements(self) -> List:
        return self._engagements

    @abstractmethod
    def add_engagement(self, engagement) -> None:
        Base.ADD_THING_TO(engagement, self.get_engagements())

    def add_engagements(self, engagements) -> None:
        Base.ADD_THINGS_TO(engagements, self.get_engagements())

    def __repr__(self) -> str:
        engagements_str = Base.__LIST_STR__(
            self.get_engagements(), ", engagements=")
        return f"{super().__repr__()}" + \
            f", type={self.get_type().name}{engagements_str}"

    DEFAULT_TEST = [
        f"Student('id=0, name=0, type=UNDERGRAD, engagements=')",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=')",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=\n----\nsmith\n----\n')",
        "N.A.",
        f"Student('id=0, name=john, type=UNDERGRAD, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')",
        UserType.UNDERGRAD
    ]

    def __whitetest__(self, results=DEFAULT_TEST) -> bool:
        assert(self.__str__() == results[0])
        self.set_name("john")
        assert(self.__str__() == results[1])
        self.add_engagement("smith")
        assert(self.__str__() == results[2])
        assert(self.get_html() == results[3])
        self.add_engagements(["doe", "jack"])
        assert(self.__str__() == results[4])
        assert(self.get_type() == results[5])
        assert(self.validate_password(User.DEFAULT_PASSWORD))
        return True
