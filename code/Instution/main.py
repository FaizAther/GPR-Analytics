from Student import Student
from Course import Course
from UserType import UserType

if __name__ == "__main__":
    u0 = Student(0, UserType.UNDERGRAD)
    u0.__whitetest__(Student.DEFAULT_TEST)
    
    u1 = Student(1, UserType.POSTGRAD)
    u2 = Student(2, UserType.PHD)
    c0 = Course(0)
    c0.add_user(u0)
    c0.add_users([u1,u2])
    c0.notify()
