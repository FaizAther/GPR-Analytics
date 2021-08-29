USE university_db;

SELECT 
interaction.total_interaction_percent,
attendance.total_attendance_percent, 
topics.topic_one_percent, topics.topic_two_percent,topics.topic_three_percent,topics.topic_four_percent,
grade.gpa
FROM student, enrolment, attendance, interaction, topics, grade
WHERE student.student_id = enrolment.student_id 
AND enrolment.enrolment_id = interaction.enrolment_id
AND enrolment.enrolment_id = attendance.enrolment_id
AND enrolment.enrolment_id = topics.enrolment_id
AND enrolment.enrolment_id = grade.enrolment_id
