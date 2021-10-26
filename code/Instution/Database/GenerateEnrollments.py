from random import randrange

password='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
i=0
for s in range(14,38):
	print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({randrange(14,24)}, {randrange(1,13)});")
	i+=1

