import random

password='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
i=0
for name in names:
	print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({random.randrange(14,24)}, {random.randrange(1,13)});")
	i+=1

