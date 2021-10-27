from Instution.Database.Database import SqliteDB

sqldb = SqliteDB()

sqldb.connection()

EVENT_ID = 0
COURSE_ID = 1
MARKED = 14
TYPE = 8
NAME = 5
MANAGER = 6
NAME = 5
STUDENT_ID = 1

ID = 0

for event in sqldb.query("SELECT * FROM Event;"):
    course_id = event[COURSE_ID]
    enrollments = sqldb.query(f"SELECT * FROM Enrollment WHERE course_id = {course_id};") # all students enroll in course with this event
    pos = 0
    attid = 0
    print('\n', f"-- Event {event[ID]}\n")
    for enrollment in enrollments:
        ms = 1
        print(
            f"INSERT INTO Attendance (position, event_id, name, marker_id, student_id, marked) " + \
            f"VALUES ({pos}, {event[EVENT_ID]}, \"Attendance for course_id: {event[COURSE_ID]}, {event[NAME]}\", {event[MANAGER]}, {enrollment[STUDENT_ID]}, {False})" \
        )
        attid += 1
        if event[MARKED] == True:
#            attendance = sqldb.query(f"SELECT * FROM Attendance WHERE event_id = {event[EVENT_ID]} and student_id = {enrollment[STUDENT_ID]};")
            print(
                f"INSERT INTO Mark (attendance_id, position, total, duedate) " + \
                f"VALUES ({attid}, {pos}, {event[EVENT_ID]}, \"Mark for course_id: {event[COURSE_ID]}, {event[NAME]}\", 30, {ms*60})" \
            )
            ms += 1
        pos += 1
