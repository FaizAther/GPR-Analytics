from __future__ import annotations

from typing import TYPE_CHECKING

from Base import Base

if TYPE_CHECKING:
    from typing import List, Dict
    from Faculty import Faculty
    from User import User

'''
	University class
'''
class University(Base):

    def __init__(self, id: int, admin=None, name=None, description=None):
        super().__init__(id, name, description)
        self._admin     :User               = admin
        self._faculties :Dict[int, Faculty] = {}
        self._users     :Dict[int, User]    = {}

    def generate_html(self) -> str:
        ## TODO
        return ""

    def get_admin(self) -> User:
        return self._admin

    def get_users(self) -> List[User]:
        return self._users

    def add_user(self, user: User) -> None:
        Base.dict_insert(user, self.get_users())

    def add_users(self, users: List[User]) -> None:
        Base.ADD_THINGS_TO(users, self.get_users())

    def get_faculties(self) -> Dict[int, Faculty]:
        return self._faculties

    def find_faculty(self, id) -> Faculty:
        return Base.dict_find(id, self.get_faculties())

    def add_faculty(self, faculty: Faculty) -> None:
        Base.dict_insert(faculty, self.get_faculties())

    def add_faculties(self, faculties: List[Faculty]) -> None:
        Base.ADD_THINGS_TO(faculties, self.get_faculties())

    def __repr__(self) -> str:
        faculties_str = Base.__LIST_STR__(
            list(self.get_faculties().values()), ", faculties=")
        return f"{super().__repr__()}" + \
            f"{faculties_str}"

    DEFAULT_TEST =[
        f"University('id=0, name=0, faculties=')",
        f"University('id=0, name=john, faculties=')",
        f"University('id=0, name=john, faculties=\n----\nsmith\n----\n')",
        "N.A.",
        f"User('id=0, name=john, faculties=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')"
    ]

    def __whitetest__(self, result=DEFAULT_TEST) -> bool:
        print(self)
        assert(self.__str__() == result[0])
        self.set_name("john")
        assert(self.__str__() == result[1])
        self.add_faculty("smith")
        print(self.__str__())
        assert(self.__str__() == result[2])
        assert(self.get_html() == result[3])
        self.add_faculties(["doe", "jack"])
        print(self.__str__())

if __name__ == "__main__":
    uni0 = University(0)
    uni0.__whitetest__()