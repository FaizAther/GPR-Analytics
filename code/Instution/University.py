from typing import List

from Base import Base
from Faculty import Faculty
from User import User

'''
	University class
'''
class University(Base):

    def __init__(self, id: int):
        super().__init__(id)
        self._faculties :List[Faculty]  = []
        self._users     :List[User]     = []

    def generate_html(self):
        ## TODO
        return ""
    
    def get_users(self):
        return self._users
    
    def add_user(self, user: User):
        Base.add_something(user, self.get_faculties())

    def add_users(self, users: List[User]):
        Base.add_somethings(users, self.get_faculties())

    def get_faculties(self):
        return self._faculties

    def add_faculty(self, faculty: Faculty):
        Base.add_something(faculty, self.get_faculties())

    def add_faculties(self, faculties: List[Faculty]):
        Base.add_somethings(faculties, self.get_faculties())

    def __repr__(self):
        return f"University('{self.__str__()}')"

    def __str__(self):
        faculties_str = Base.__LIST_STR__(
            self.get_faculties(), ", faculties=")
        return super().__str__() + faculties_str
    
    def __whitetest__(self, result):
        print(self.__repr__())
        assert(self.__repr__() == result[0])
        self.set_name("john")
        assert(self.__repr__() == result[1])
        self.add_faculty("smith")
        print(self.__repr__())
        assert(self.__repr__() == result[2])
        assert(self.get_html() == result[3])
        self.add_faculties(["doe", "jack"])
        print(self.__repr__())
    
if __name__ == "__main__":
    uni0 = University(0)
    uni0.__whitetest__(result=[
        f"University('id=0, name=0, faculties=')",
        f"University('id=0, name=john, faculties=')",
        f"University('id=0, name=john, faculties=\n----\nsmith\n----\n')",
        "",
        f"User('id=0, name=john, faculties=\n----\nsmith\n----\n\n----\ndoe\n----\n\n----\njack\n----\n')"
    ])
