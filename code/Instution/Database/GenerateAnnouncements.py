



from datetime import datetime
i=0
for course_id in range(1, 13):
	print(f"INSERT INTO Announcement (course_id, position, created, description) VALUES ({course_id}, {i},{datetime.now()}, \"Welcome to week 1!\"") 
	#i += 1