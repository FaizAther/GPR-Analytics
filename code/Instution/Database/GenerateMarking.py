from Instution.Database.Database import SqliteDB

sqldb = SqliteDB()

sqldb.connection()

EVENT_ID = 0
COURSE_ID = 1
MARKED = 14
TYPE = 8
NAME = 5
MANAGER = 6

STUDENT_ID = 1

for event in sqldb.query("SELECT * FROM Event;"):
    course_id = event[COURSE_ID]
    enrollments = sqldb.query(f"SELECT * FROM Enrollment WHERE course_id = {course_id};") # all students enroll in course with this event
    pos = 0
    for enrollment in enrollments:
        if event[MARKED] == True: # Attendance
            #print(event[NAME])
            print(
                f"INSERT INTO Attendance (position, event_id, name, marker_id, student_id, marked) " + \
                f"VALUES ({pos}, {event[EVENT_ID]}, \"Attendance {pos}\", {event[MANAGER]}, {enrollment[STUDENT_ID]}, {False})" \
            )
        else: # Mark
            print(
                f"INSERT INTO Attendance (position, event_id, name, marker_id, student_id, marked) " + \
                f"VALUES ({pos}, {event[EVENT_ID]}, \"Attendance {pos}\", {event[MANAGER]}, {enrollment[STUDENT_ID]}, {False})" \
            )
            print(
                f"INSERT INTO Mark (attendance_id, position, event_id, name, marker_id, student_id, marked) " + \
                f"VALUES ({pos}, {event[EVENT_ID]}, \"Attendance {pos}\", {event[MANAGER]}, {enrollment[STUDENT_ID]}, {False})" \
            )
        pos += 1
