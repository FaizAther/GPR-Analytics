

from datetime import datetime, timedelta
from random import randrange
'''
CREATE TABLE Event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    created_date date NOT NULL,
    description text,
    name text NOT NULL,
    manager_id INTEGER NOT NULL,
    resource_id INTEGER,
    type INTEGER NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    reacurring NOT NULL,
    day_of_week INTEGER,
    time_of_day INTEGER,
    foreign key (resource_id) references Resource(id),
    foreign key (manager_id) references User(id),
    foreign key (course_id) references Course(id)
);
'''

from Instution.Events.EventType import EventType

def courses_events():
	for course_id in range(1,13):
		print(f"\n-- Course {course_id}\n")
		events(course_id)

def events(course_id):
	manager_id = course_id + 1
	
	position = 0
	for event_num in range(1,4):

		event_reacurring(course_id, position, manager_id, event_num, EventType.LECTURE, False)
		position+=1
		# Attendance for each student
		event_reacurring(course_id, position, manager_id, event_num, EventType.TUTORIAL, False)
		position+=1
		# Attendance for each student
		event_reacurring(course_id, position, manager_id, event_num, EventType.PRACTICAL, False)
		position+=1
		# Attendance for each student
		event_once(course_id, position, manager_id, event_num, EventType.ASSIGNMENT, True)
		position+=1
		# Attendance for each student

		# Marking for each student

	event_reacurring(course_id, position, manager_id, 1, EventType.CONSULTATION, False)
	position+=1

	event_once(course_id, position, manager_id, 1, EventType.EXAM, True)
	position+=1
	# Attendance for each student

def event_once(course_id, position, manager_id, event_num, event_type, marked):
	event(course_id, position, manager_id, event_num, event_type, False, None, None, marked)

def event_reacurring(course_id, position, manager_id, event_num, event_type, marked):
	event(course_id, position, manager_id, event_num, event_type, True, randrange(0, 6), randrange(0, 10), marked)

def event(course_id, position, manager_id, event_num, event_type, reacurring, day_of_week, time_of_day, marked):
	
	print(\
		f"INSERT INTO Event (course_id, position, created_date, name, " + \
		f"manager_id, type, start_date, end_date, reacurring, marked"+ \
		(f"" if not reacurring else f", day_of_week, time_of_day") + \
		f") " + \
		f"VALUES ({course_id}, {position}, \"{datetime.now()}\", \"{event_type.name} {event_num}\", " + \
		f"{manager_id}, {event_type.value}, \"{datetime.now()}\", \"{datetime.now() + timedelta(days=6*30)}\", {reacurring}, {marked}" + \
		(f"" if not reacurring else f", {day_of_week}, {time_of_day}") + \
		f");"\
	)


#def attendance()

courses_events()











