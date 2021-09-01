from University import University
from Course import Course
from Student import Student
from Tutor import Tutor
from Lecturer import Lecturer
from UserType import UserType
from EventType import EventType
from Event import Event
from Mark import Mark

if __name__ == "__main__":
    uni0 = University(0, "UniQLD", "Purple")
    #print(uni0)
    u0 = Student(100)
    #print(u0)

    u1 = Student(101, UserType.POSTGRAD)
    u2 = Student(102, UserType.PHD)

    u3 = Student(104)


    t0 = Tutor(300)

    l0 = Lecturer(400)

    c0 = Course(500)
    c0.add_user(l0)

    #print("admin is: ", c0.get_admin())

    #print(c0)
    c0.add_user(u0)
    c0.add_users([u1,u2])
    c0.add_user(t0)
    #c0.notify()

    e0 = Event(700, type=EventType.ASSIGNMENT)
    e0.set_weighting(5)

    print(t0.get_capacity())

    e0.add_users([l0,t0,u0,u1,u2,u3])

    print(t0.get_capacity())

    print(u0)