from random import randrange

password='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
i=0
for s in range(14,38):
	# 3 courses per student
	random_subs = []
	while len(random_subs) < 3:
		my_sub = randrange(1,13)
		if my_sub not in random_subs:
			print(f"INSERT INTO Enrollment (user_id, course_id) VALUES ({s}, {my_sub});")
			random_subs.append(my_sub)
	i+=1

