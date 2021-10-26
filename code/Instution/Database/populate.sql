
-- User
-- INSERT INTO User Values (id, pos, uni_id, name, type, password);

-- University
-- INSERT INTO University Values (id, name, admin_id)

-- Faculty
-- INSERT INTO Faculty Values (id, pos, uni_id, name, type, password);


-- Add The Univeristy of Queensland
INSERT INTO University (name, admin, description) VALUES ("The Univeristy of Queensland", 0, "Purple is the best!");

-- Add Admin user
INSERT INTO User (position, university_id, name, type, password) VALUES (0, 0, "John", 8, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Faculty

INSERT INTO Faculty (position, university_id, name, dean) VALUES (0, 1, "COMP", 1);
INSERT INTO Faculty (position, university_id, name, dean) VALUES (1, 1, "MATH", 2);
INSERT INTO Faculty (position, university_id, name, dean) VALUES (2, 1, "PHYS", 1);
INSERT INTO Faculty (position, university_id, name, dean) VALUES (3, 1, "STAT", 1);


-- Add Courses


-- COMP
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 1, "COMP-3301", 0);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 1, "COMP-4403", 1);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 1, "COMP-3301", 2);

-- MATH
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 2, "MATH-1081", 3);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 2, "MATH-1131", 4);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 2, "MATH-1231", 5);

-- PHYS
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 3, "PHYS-1111", 6);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 3, "PHYS-2222", 7);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 3, "PHYS-3333", 8);

-- STAT
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 4, "STAT-1100", 9);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 4, "STAT-2200", 10);
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 4, "STAT-3300", 11);

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

INSERT INTO User (position, university_id, name, type, password) VALUES (0, 1, "Solomen", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (1, 1, "Simon", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (2, 1, "Joseph", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (3, 1, "Lazarus", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (4, 1, "Judas", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (5, 1, "Yeshua", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (6, 1, "Ananias", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (7, 1, "Jonathan", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (8, 1, "Aaron", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (9, 1, "Nathaniel", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (10, 1, "Ezra", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (11, 1, "Asher", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (12, 1, "Jacob", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (13, 1, "Caleb", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (14, 1, "Noah", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (15, 1, "Zachary", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (16, 1, "Jonah", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (17, 1, "Isaac", 5, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (18, 1, "Eli", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (19, 1, "Benjamin", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (20, 1, "Rebecca", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (21, 1, "Elizabeth", 6, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (22, 1, "Mary", 4, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");
INSERT INTO User (position, university_id, name, type, password) VALUES (23, 1, "Joshua", 7, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Tutor TODO

-- Add Enrollments
--INSERT INTO Enrollment (user_id, course_id) VALUES (x, y)
INSERT INTO Enrollment (user_id, course_id) VALUES (20, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (21, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 2);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (21, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (14, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (20, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (18, 11);
INSERT INTO Enrollment (user_id, course_id) VALUES (14, 9);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 5);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 3);
INSERT INTO Enrollment (user_id, course_id) VALUES (15, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (23, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (16, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 7);
INSERT INTO Enrollment (user_id, course_id) VALUES (22, 1);
INSERT INTO Enrollment (user_id, course_id) VALUES (17, 12);
INSERT INTO Enrollment (user_id, course_id) VALUES (16, 10);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 8);
INSERT INTO Enrollment (user_id, course_id) VALUES (19, 11);

-- Add Announcements

INSERT INTO Announcement (course_id, position, created, description) VALUES (1, 0, "2021-10-26 16:28:17.303301", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (2, 0, "2021-10-26 16:28:17.303333", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (3, 0, "2021-10-26 16:28:17.303338", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (4, 0, "2021-10-26 16:28:17.303341", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (5, 0, "2021-10-26 16:28:17.303345", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (6, 0, "2021-10-26 16:28:17.303348", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (7, 0, "2021-10-26 16:28:17.303351", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (8, 0, "2021-10-26 16:28:17.303354", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (9, 0, "2021-10-26 16:28:17.303358", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (10, 0, "2021-10-26 16:28:17.303365", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (11, 0, "2021-10-26 16:28:17.303368", "Welcome to week 1!");
INSERT INTO Announcement (course_id, position, created, description) VALUES (12, 0, "2021-10-26 16:28:17.303371", "Welcome to week 1!");


-- Add Events
















