from __future__ import annotations

from typing import TYPE_CHECKING

from Instution.Base import Base
from Instution.Universities.Faculty import Faculty
from Instution.Users.Lecturer import Lecturer
from Instution.Users.Student import Student
from Instution.Users.Tutor import Tutor
from Instution.Users.UserType import UserType

if TYPE_CHECKING:
    from typing import List, Dict
    from Instution.Users.User  import User

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
        return super().generate_html()

    def get_admin(self) -> User:
        return self._admin

    def get_users(self) -> Dict[User]:
        return self._users

    def make_user(self, type: UserType, name: str=None, description=None) -> User:
        position = len(self.get_users().values())

        if type == UserType.LECTURER:
            user = Lecturer(position)
        elif type == UserType.TUTOR:
            user = Tutor(position)
        elif type == UserType.STUDENT or type == UserType.UNDERGRAD:
            user = Student(position)
        elif type == UserType.POSTGRAD:
            user = Student(position, type=type)
        elif type == UserType.PHD:
            user = Student(position, type=type)
    
        self.add_user(user)
        return user

    def add_user(self, user: User) -> None:
        Base.dict_insert(user, self.get_users())

    def add_users(self, users: Dict[User]) -> None:
        Base.__DO_SOMETHINGS__(lambda u: self.add_user(u), users)

    def get_faculties(self) -> Dict[int, Faculty]:
        return self._faculties

    def get_faculties_list(self) -> List[Faculty]:
        return self.get_faculties().values()

    def find_faculty(self, id) -> Faculty:
        return Base.dict_find(id, self.get_faculties())

    def find_user(self, id) -> User:
        return self.get_admin() if id == "admin" else Base.dict_find(id, self.get_users())

    def make_faculty(self, name: str=None, description=None) -> Faculty:
        faculty = Faculty(len(self.get_faculties().values()), name=name, description=description)
        print(self)
        self.add_faculty(faculty)
        return faculty

    def add_faculty(self, faculty: Faculty) -> None:
        Base.dict_insert(faculty, self.get_faculties())

    def add_faculties(self, faculties: Dict[Faculty]) -> None:
        Base.__DO_SOMETHINGS__(lambda f: self.add_faculty(f), faculties)


    def insert(self) -> str:
        return super().insert()

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