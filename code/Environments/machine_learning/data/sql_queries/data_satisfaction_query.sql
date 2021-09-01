USE university_db;

SELECT 
enrolment.enrolment_id, interaction.total_interaction_percent,
attendance.total_attendance_percent, 
satisfaction.survey_rating_percent, satisfaction.satisfaction_rate_percent,
satisfaction.is_satisfied
FROM student, enrolment, attendance, interaction, satisfaction
WHERE student.student_id = enrolment.student_id 
AND enrolment.enrolment_id = interaction.enrolment_id
AND enrolment.enrolment_id = attendance.enrolment_id
AND enrolment.enrolment_id = satisfaction.enrolment_id
