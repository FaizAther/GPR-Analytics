from University import University
from Course import Course
from Student import Student
from Tutor import Tutor
from Lecturer import Lecturer
from UserType import UserType

if __name__ == "__main__":
    uni0 = University(0, "UniQLD", "Purple")
    print(uni0)
    u0 = Student(0)
    print(u0)

    u1 = Student(1, UserType.POSTGRAD)
    u2 = Student(2, UserType.PHD)

    t0 = Tutor(33)

    l0 = Lecturer(4)

    c0 = Course(0)
    c0.add_user(l0)

    print("admin is: ", c0.get_admin())

    print(c0)
    c0.add_user(u0)
    c0.add_users([u1,u2])
    c0.add_user(t0)
    c0.notify()
