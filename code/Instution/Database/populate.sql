
-- User
-- INSERT INTO User Values (id, pos, uni_id, name, type, password);

-- University
-- INSERT INTO University Values (id, name, admin_id)

-- Faculty
-- INSERT INTO Faculty Values (id, pos, uni_id, name, type, password);


-- Add The Univeristy of Queensland
INSERT INTO University (name, admin, description) VALUES ("The Univeristy of Queensland", 1, "Purple is the best!");

-- Add Admin user
INSERT INTO User (position, university_id, name, type, password) VALUES (0, 0, "John", 8, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Faculty

INSERT INTO Faculty (position, university_id, name, dean_id, description) VALUES (0, 1, "COMP", 1, "The Faculty of Computer Science");
INSERT INTO Faculty (position, university_id, name, dean_id, description) VALUES (1, 1, "MATH", 2, "The Faculty of Mathematics");
INSERT INTO Faculty (position, university_id, name, dean_id, description) VALUES (2, 1, "PHYS", 1, "The Faculty of Physics");
INSERT INTO Faculty (position, university_id, name, dean_id, description) VALUES (3, 1, "STAT", 1, "The Faulty of Statistics");


-- Add Courses


-- COMP
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (3301, 1, "COMP-3301", 2);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (4403, 1, "COMP-4403", 3);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (4506, 1, "COMP-4506", 4);

-- MATH
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (1081, 2, "MATH-1081", 5);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (1131, 2, "MATH-1131", 6);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (1231, 2, "MATH-1231", 7);

-- PHYS
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (1111, 3, "PHYS-1111", 8);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (2222, 3, "PHYS-2222", 9);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (3333, 3, "PHYS-3333", 10);

-- STAT
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (0, 4, "STAT-1100", 11);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (1, 4, "STAT-2200", 12);
INSERT INTO Course (position, faculty_id, name, coordinator_id) VALUES (2, 4, "STAT-3300", 13);

-- Add Lecturer

INSERT INTO User (position, university_id, name, type, password) VALUES (0, 1, "Bill Gates", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (1, 1, "Richard Stallman", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (2, 1, "Ian Hayes", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (3, 1, "Al Ghazali", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (4, 1, "Aristotle", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (5, 1, "Socrates", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (6, 1, "Mohammad Hijab", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (7, 1, "Albert Einstein", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (8, 1, "Nikola Tesla", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (9, 1, "Mohammad bin Nayeb", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (10, 1, "Bin Salman", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (11, 1, "Ahsan Virani", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Students

INSERT INTO User (position, university_id, name, type, password) VALUES (12, 1, "Solomen", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (13, 1, "Simon", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (14, 1, "Joseph", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (15, 1, "Lazarus", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (16, 1, "Judas", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (17, 1, "Yeshua", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (18, 1, "Ananias", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (19, 1, "Jonathan", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (20, 1, "Aaron", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (21, 1, "Nathaniel", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (22, 1, "Ezra", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (23, 1, "Asher", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (24, 1, "Jacob", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (25, 1, "Caleb", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (26, 1, "Noah", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (27, 1, "Zachary", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (28, 1, "Jonah", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (29, 1, "Isaac", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (30, 1, "Eli", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (31, 1, "Benjamin", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (32, 1, "Rebecca", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (33, 1, "Elizabeth", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (34, 1, "Mary", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (35, 1, "Joshua", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Tutor TODO

-- Add Enrollments
--INSERT INTO Enrollment (user_id, course_id) VALUES (x, y)
INSERT INTO Enrollment (user_id, course_id) VALUES (14, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (14, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (14, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (15, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (15, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (15, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (16, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (16, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (16, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (18, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (18, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (18, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (20, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (20, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (20, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (21, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (21, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (21, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (23, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (23, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (23, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (24, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (24, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (24, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (25, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (25, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (25, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (26, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (26, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (26, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (27, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (27, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (27, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (28, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (28, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (28, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (29, 6);
INSERT INTO Enrollment (user_id, course_id) VALUES (29, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (29, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (30, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (30, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (30, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (31, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (31, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (31, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (32, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (32, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (32, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (33, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (33, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (33, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (34, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (34, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (34, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (35, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (35, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (35, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (36, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (36, 4);
INSERT INTO Enrollment (user_id, course_id) VALUES (36, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (37, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (37, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (37, 12);







-- Add Announcements

INSERT INTO Announcement (course_id, position, created_date, description) VALUES (1, 0, "2021-10-26 16:28:17.303301", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (2, 0, "2021-10-26 16:28:17.303333", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (3, 0, "2021-10-26 16:28:17.303338", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (4, 0, "2021-10-26 16:28:17.303341", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (5, 0, "2021-10-26 16:28:17.303345", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (6, 0, "2021-10-26 16:28:17.303348", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (7, 0, "2021-10-26 16:28:17.303351", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (8, 0, "2021-10-26 16:28:17.303354", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (9, 0, "2021-10-26 16:28:17.303358", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (10, 0, "2021-10-26 16:28:17.303365", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (11, 0, "2021-10-26 16:28:17.303368", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created_date, description) VALUES (12, 0, "2021-10-26 16:28:17.303371", "Welcome to week 1!");


-- Add Events

-- Add 3 Lectures b/w 9 to 16 hundred hours 1 hour each randomly

-- Add 1 Consultation b/w 9 to 16 hundred hours 1 hour each randomly

-- Add 3 Tutorials b/w 9 to 16 hundred hours 1 hour each randomly

-- Add 3 Pracs b/w 9 to 16 hundred hours 1 hour each randomly

-- Add 3 to 4 Markings 150 days semester divide accordingly for deadlines

-- Add 1 Exam each +160 days deadline















