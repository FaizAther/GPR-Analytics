from Base import Base
from University import University
from Faculty import Faculty
from Course import Course
from Student import Student
from Tutor import Tutor
from Lecturer import Lecturer
from UserType import UserType
from EventType import EventType
from Event import Event
from Mark import Mark

uni0 = University(0, name="UniQLD", description="Purple")
#print(uni0)
u0 = Student(100)
#print(u0)

u1 = Student(101, UserType.POSTGRAD)
u2 = Student(102, UserType.PHD)

u3 = Student(104)


t0 = Tutor(300)
l0 = Lecturer(400)

uni0.add_users([u0,u1,u2,u3,t0,l0])

f0 = Faculty(0, name="COMP")
uni0.add_faculty(f0)
f0.make_course(3301)
f0.add_user(u0, 3301)
f0.add_user(l0, 3301)

f0.make_course(4403)

#print("admin is: ", Base.dict_find(3301, f0.get_courses()).get_admin())

#print(c0)
f0.add_users([u1,u2], 3301)
f0.add_user(t0, 3301)
#c0.notify()
print(f0.get_courses().values())
print("here")
c0 = Base.dict_find(3301, f0.get_courses())
e0 = c0.update(l0)
e0.set_type(EventType.ASSIGNMENT)
c0.notify(e0)
#e0 = Event(700, type=EventType.ASSIGNMENT)
e0.set_weighting(5)

#print(t0.get_capacity())

e0.add_users([l0,t0,u0,u1,u2,u3])

#print(t0.get_capacity())

#print(u0)
