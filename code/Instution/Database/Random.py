import random

names = ["Solomen",
"Simon",
"Joseph",
"Lazarus",
"Judas",
"Yeshua",
"Ananias",
"Jonathan",
"Aaron",
"Nathaniel",
"Ezra",
"Asher",
"Jacob",
"Caleb",
"Noah",
"Zachary",
"Jonah",
"Isaac",
"Eli",
"Benjamin",
"Rebecca",
"Elizabeth",
"Mary",
"Joshua"]

student=[4,5,6,7]
password='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
i=0
for name in names:
	print(f"INSERT INTO User (position, university_id, name, type, password) VALUES ({i}, 0, \"{name}\", {random.randrange(4,8)}, \"{password}\");")
	i+=1