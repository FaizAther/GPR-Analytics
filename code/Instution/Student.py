from User import User
from Course import Course
from UserType import UserType

class Student(User):
    def __init__(self, id: int, type: UserType=UserType.UNDERGRAD):
        super().__init__(id, type)
    
    def generate_html(self):
        return ""
    
    def update(self, course: Course):
        print(self.get_type().__str__() + self.get_id().__str__() + "in update")