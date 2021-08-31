from University import University
from Course import Course
from Student import Student
from UserType import UserType

if __name__ == "__main__":
    uni0 = University(0, "UniQLD", "Purple")
    print(uni0)
    u0 = Student(0, UserType.UNDERGRAD)
    print(u0)
    u0.__whitetest__()
    u1 = Student(1, UserType.POSTGRAD)
    u2 = Student(2, UserType.PHD)

    
    c0 = Course(0)
    c0.add_user(u0)
    c0.add_users([u1,u2])
    c0.notify()
