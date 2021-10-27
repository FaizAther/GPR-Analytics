from enum import unique
from Instution.PrettifyMe.BuilderHTML import BuilderHTML
from Instution.Base import Base
from Instution.Universities.University import University
from Instution.Universities.Faculty import Faculty
from Instution.Universities.Course import Course
from Instution.Users.Student import Student
from Instution.Users.Tutor import Tutor
from Instution.Users.Lecturer import Lecturer
from Instution.Users.UserType import UserType
from Instution.Events.EventType import EventType
from Instution.Events.Event import Event
from Instution.Events.Mark import Mark
from Instution.Users.Sudo import Sudo
from Instution.Database.Database import SqliteDB

import datetime

sqldb = SqliteDB()
# sqldb.connection()

# Create the sudo user

my_sudo = Sudo()
# print(my_sudo)

# Populate admins

admins_query = sqldb.query(f"Select * FROM User WHERE type = {UserType.ADMIN.value}")

for admin_query in admins_query:
    # Find Uni
    uni_query = sqldb.query(f"Select * FROM University WHERE admin = {admin_query[0]}")[0]
    # print(uni_query)
    # Make admin
    my_admin = my_sudo.add_admin(name=uni_query[1], description=uni_query[3])
    my_uni = my_admin.get_university()
    # Add Users

    user_queries = sqldb.query_dict(f"Select * FROM User")
    for user_query in user_queries:
        my_user = my_uni.make_user(UserType(user_query['type']), name=user_query['name'], description=user_query['description'])
        #print(my_user)

    # Find Faculties
    facs_query = sqldb.query(f"Select * FROM Faculty WHERE university_id = {uni_query[0]}")
    # print(facs_query)
    for fac_query in facs_query:
        # print(fac_query)
        my_fac = my_uni.make_faculty(name=fac_query[3], description=fac_query[5])
        # print("FUCK")
        courses_query = sqldb.query_dict(f"Select * FROM Course WHERE faculty_id = {fac_query[0]}")
        for course_query in courses_query:
            # print(course_query)
            coordinator_id = course_query['coordinator_id']
            coordinaotr_query = sqldb.query_dict(f"Select * FROM User WHERE id = {coordinator_id}")[0]
            # print(coordinator_id, coordinaotr_query)
            my_course_admin = my_uni.find_user(int(coordinaotr_query['position']))
            # print(my_course_admin)
            my_course = my_fac.make_course(id=course_query['position'], name=course_query['name'], admin=my_course_admin)

            annon_queries = sqldb.query_dict(f"Select * FROM Announcement WHERE course_id = {course_query['id']}")

            # Add announcements
            for annon_querry in annon_queries:
                check_annon = my_course.make_announcement(annon_querry['position'], time=annon_querry['created_date'], description=annon_querry['description'])
            # print(my_course.get_announcements())
            # Enroll students
            enroll_querries = sqldb.query_dict(f"Select * FROM Enrollment WHERE course_id = {course_query['id']}")
            for enroll_query in enroll_querries:
                # print("Enrollment -q", enroll_query)
                user_querry = sqldb.query_dict(f"Select * FROM User where id = {enroll_query['user_id']}")[0]
                # print("User -q", user_querry)
                # print(my_uni.get_users()[user_querry['position']])
                # print(my_course)
                my_course.add_user(my_uni.get_users()[user_querry['position']])

            event_querries = sqldb.query_dict(f"Select * FROM Event WHERE course_id = {course_query['id']}")
            for event_querry in event_querries:
                print(event_querry)
    

            # print(my_uni.get_users())
            event_queries = sqldb.query_dict(f"Select * FROM Event WHERE course_id = {course_query['id']}")
            
            
            deadline = datetime.datetime.fromisoformat(event_queries[0]['start_date'])
            for event_query in event_queries:
                event = my_course.make_event(event_query['position'], event_query['type'], \
                    event_query['name'], event_query['start_date'], event_query['end_date'], (30 if event_query['marked'] else 0), deadline=deadline)
                if event_query['marked']:
                    deadline += datetime.timedelta(days=50)
                # print(deadline)
                # print(event_query)
                # print(event.get_invitees())
            

            # pass
        # print(my_fac.get_courses_list())
        # print(my_fac)

# print(my_user.get_engagements())
# for engagement in my_user.get_engagements():
#     print(engagement)
# print(my_user.get_specific_engagement(my_course))
# Populate University

# Populate Faculty

# Populate Courses

# Populate Events


# Populate Users for The University of Queensland

# users_query = sqldb.query(f"Select * FROM User")

# for user_query in users_query:
    # print(user_query)


# my_admin = my_sudo.add_admin(name="UQ", description="Purple")
# print(my_admin)
# my_admin2 = my_sudo.add_admin(name="UNSW", description="Yellow")
# print(my_admin2)
# uni0 = my_admin.get_university()
# print(uni0)
# my_faculty = uni0.make_faculty("COMP")
# print(my_faculty)
# course = my_faculty.make_course_annon()
# print(course)
# print(my_faculty)

# #print(uni0)
# u0 = uni0.make_user(UserType.UNDERGRAD)
# #print(u0)

# u1 = uni0.make_user(UserType.POSTGRAD)
# u2 = uni0.make_user(UserType.PHD)

# u3 = uni0.make_user(UserType.UNDERGRAD)


# t0 = uni0.make_user(UserType.TUTOR)
# l0 = uni0.make_user(UserType.LECTURER)

# f0 = uni0.make_faculty("COMP", description="The most fun")
# f0.make_course(3301)
# f0.add_user(u0, 3301)
# print("FUCKKK", u0.get_enrollments())
# f0.add_user(l0, 3301)

# f0.make_course(4403)

# #print("admin is: ", Base.dict_find(3301, f0.get_courses()).get_admin())

# #print(c0)
# f0.add_users([u1,u2], 3301)
# f0.add_user(t0, 3301)
# #c0.notify()
# print(f0.get_courses().values())
# print("here")
# c0 = Base.dict_find(3301, f0.get_courses())
# e0 = c0.update(l0)
# e0.set_type(EventType.ASSIGNMENT)
# c0.notify(e0)
# #e0 = Event(700, type=EventType.ASSIGNMENT)
# e0.set_weighting(5)

# #print(t0.get_capacity())

# e0.add_users([l0,t0,u0,u1,u2,u3])

# #print(t0.get_capacity())

# #print(u0)

# print(uni0.get_users())

# print(uni0.generate_html())