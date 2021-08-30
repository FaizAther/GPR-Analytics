from abc import abstractmethod
from Base       import Base
from UserType   import UserType
from typing     import List
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
        self._engagements   :List   = []
        self._password      :str    = ""
        self.set_password(User.DEFAULT_PASSWORD)
        self._type:UserType = type
    
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
        self.get_engagements().append(engagement)

    def add_engagements(self, engagements) -> None:
        for e in engagements:
            self.add_engagement(e)

    def __repr__(self) -> str:
        return f"{self.get_type().name}('{self.__str__()}')"

    def __str__(self) -> str:
        engagements_str = Base.__LIST_STR__(
            self.get_engagements(), ", engagements=")    
        return super().__str__() + engagements_str

    def __whitetest__(self, results) -> bool:
        assert(self.__repr__() == results[0])
        self.set_name("john")
        assert(self.__repr__() == results[1])
        self.add_engagement("smith")
        assert(self.__repr__() == results[2])
        assert(self.get_html() == results[3])
        self.add_engagements(["doe", "jack"])
        assert(self.__repr__() == results[4])
        assert(self.get_type() == results[5])
        assert(self.validate_password(User.DEFAULT_PASSWORD))
        return True

if __name__ == "__main__":
    u0 = User(0, UserType.UNDERGRAD)
    u0.__whitetest__([
        f"UNDERGRAD('id=0, name=0, engagements=')",
        f"UNDERGRAD('id=0, name=john, engagements=')",
        f"UNDERGRAD('id=0, name=john, engagements=\n----\nsmith\n----\n')",
        "",
        f"UNDERGRAD('id=0, name=john, engagements=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')",
        UserType.UNDERGRAD
    ])

