



from datetime import datetime
i=0
for course_id in range(1, 13):
	for i in range(0,6):
		print(f"INSERT INTO Announcement (course_id, position, created_date, description) VALUES ({course_id}, {i}, \"{datetime.now()}\", \"Welcome to week {i+1}!\");") 
	#i += 1