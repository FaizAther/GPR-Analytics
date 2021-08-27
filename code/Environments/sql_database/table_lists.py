def tables():

    TABLES = {}
    TABLES['Student'] = (
    "CREATE TABLE `Student` ("
    "  `student_id` int(20) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(100) NOT NULL,"
    "  `age` int(10) NOT NULL,"
    "  `degree` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")

    TABLES['Goals'] = (
    "CREATE TABLE `Goals` ("
    "  `student_id` int(20) NOT NULL AUTO_INCREMENT,"
    "  `gpa` int(10) NOT NULL,"
    "  `lec_attendance` int(100) NOT NULL,"
    "  `tut_attendance` varchar(100) NOT NULL,"
    "  FOREIGN KEY(student_id) REFERENCES Student(student_id)"
    ") ENGINE=InnoDB")

    TABLES['Course'] = (
    "CREATE TABLE `Course` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `name` varchar(50) NOT NULL,"
    "  `level` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`course_id`)"
    ") ENGINE=InnoDB")

    TABLES['Topics'] = (
    "CREATE TABLE `Topics` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `topic_one_percent` int(100) NOT NULL,"
    "  `topic_two_percent` int(100) NOT NULL,"
    "  `topic_three_percent` int(100) NOT NULL,"
    "  `topic_four_percent` int(100) NOT NULL,"
    "  FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Course_statistic'] = (
    "CREATE TABLE `Course_statistic` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `pass_rate_percent` int(100) NOT NULL,"
    "  `drop_out_percent` int(100) NOT NULL,"
    "  `real_world_app_percent` int(100) NOT NULL,"
    "  `effectiveness_percent` int(100) NOT NULL,"
    "  FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['Enrolment'] = (
    "CREATE TABLE `Enrolment` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `student_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `enrol_date` date NOT NULL,"
    "  `study_type` varchar(20) NOT NULL,"
    "   PRIMARY KEY (`enrolment_id`),"
    "   FOREIGN KEY(student_id) REFERENCES Student(student_id),"
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['Satisfaction'] = (
    "CREATE TABLE `Satisfaction` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `satisfaction_rate_percent` int(100) NOT NULL,"
    "  `survey_rating_percent` int(100) NOT NULL,"
    "  `is_satisfied` Boolean NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Interaction'] = (
    "CREATE TABLE `Interaction` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `lec_interaction_percent` int(100) NOT NULL,"
    "  `tut_interaction_percent` int(100) NOT NULL,"
    "  `total_interaction_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Grade'] = (
    "CREATE TABLE `Grade` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `gpa` int(100) NOT NULL,"
    "  `at_risk` Boolean NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")
   
    TABLES['Assessments'] = (
    "CREATE TABLE `Assessments` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `mid_sem_exam_percent` int(100) NOT NULL,"
    "  `quiz_score_percent` int(100) NOT NULL,"
    "  `assignment_score_percent` int(100) NOT NULL,"
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Attendance'] = (
    "CREATE TABLE `Attendance` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `lec_attendance_percent` int(100) NOT NULL,"
    "  `tut_attendance_percent` int(100) NOT NULL,"
    "  `personal_study_percent` int(100) NOT NULL,"
    "  `lec_incompletion_percent` int(100) NOT NULL,"
    "  `tut_incompletion_percent` int(100) NOT NULL,"
    "  `total_attendance_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")


    return TABLES
