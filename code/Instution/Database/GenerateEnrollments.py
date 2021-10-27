from random import randrange

password='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
i=0
for s in range(14,38):
	# 3 courses per student
	print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({s}, {randrange(1,13)});")
	print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({s}, {randrange(1,13)});")
	print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({s}, {randrange(1,13)});")
	i+=1

