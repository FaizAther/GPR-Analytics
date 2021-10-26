
-- User
-- INSERT INTO User Values (id, pos, uni_id, name, type, password);

-- University
-- INSERT INTO University Values (id, name, admin_id)

-- Faculty
-- INSERT INTO Faculty Values (id, pos, uni_id, name, type, password);


-- Add The Univeristy of Queensland
INSERT INTO University (name, admin, description) VALUES ("The Univeristy of Queensland", 0, "Purple is the best!");

-- Add Admin user
INSERT INTO User (id, position, university_id, name, type, password) VALUES (0, 0, 0, "John", 8, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Faculty

INSERT INTO Faculty (position, university_id, name, dean) VALUES (0, 0, "COMP", 1);

INSERT INTO Faculty (position, university_id, name, dean) VALUES (1, 0, "MATH", 2);

INSERT INTO Faculty (position, university_id, name, dean) VALUES (2, 0, "PHYS", 1);

-- Add Courses


-- COMP
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 0, "COMP-3301", 1);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 0, "COMP-4403", 10);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 0, "COMP-3301", 2);

-- MATH
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 1, "MATH-1081", 0);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 1, "MATH-1131", 7);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 1, "MATH-1231", 3);

-- PHYS
INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (0, 2, "PHYS-1111", 8);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (1, 2, "PHYS-2222", 9);

INSERT INTO Course (position, faculty_id, name, coordinator) VALUES (2, 2, "PHYS-3333", 6);

-- Add Lecturer

INSERT INTO User (position, university_id, name, type, password) VALUES (0, 0, "Al Ghazali", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (1, 0, "Ross", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (2, 0, "Matt", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (3, 0, "Bin Salman", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (4, 0, "Mohammad bin Nayeb", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (5, 0, "Mohammad Hijab", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (6, 0, "Aristotle", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (7, 0, "Socrates", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (8, 0, "Richard Stallman", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (9, 0, "Bill Gates", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

INSERT INTO User (position, university_id, name, type, password) VALUES (10, 0, "Ian Hayes", 0, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8");

-- Add Tutor

-- Add Students
