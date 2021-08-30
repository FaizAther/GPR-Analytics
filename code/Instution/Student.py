from User import User
from Course import Course
from UserType import UserType

class Student(User):
    def __init__(self, id: int, type: UserType=UserType.UNDERGRAD):
        super().__init__(id, type)
    
    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        print(self.get_type().__str__() + self.get_id().__str__() + " in update")

    
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