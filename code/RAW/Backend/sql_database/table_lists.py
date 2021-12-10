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
    "  `mid_sem_survey_rating_percent` int(100) NOT NULL,"
    "  `final_survey_rating_percent` int(100) NOT NULL,"
    "  `is_satisfied` Boolean NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Grade'] = (
    "CREATE TABLE `Grade` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `gpa` int(100) NOT NULL,"
    "  `at_risk` Boolean NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    TABLES['Attendance'] = (
    "CREATE TABLE `Attendance` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `lec_attendance_percent` int(100) NOT NULL,"
    "  `tut_attendance_percent` int(100) NOT NULL,"
    "  `lec_incompletion_percent` int(100) NOT NULL,"
    "  `tut_incompletion_percent` int(100) NOT NULL,"
    "  `total_attendance_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id)"
    ") ENGINE=InnoDB")

    ########### THIS SECTION IS FOR ADDING COURSES ########### 
    TABLES['CSSE2010'] = (
    "CREATE TABLE `CSSE2010` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `weekly_quiz` int(100) NOT NULL,"
    "  `assignment_1` int(100) NOT NULL,"
    "  `assignment_2` int(100) NOT NULL,"
    "  `final_exam` int(100) NOT NULL,"
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['COMP3506'] = (
    "CREATE TABLE `COMP3506` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `weekly_quiz` int(100) NOT NULL," #20
    "  `Project` int(100) NOT NULL," #30
    "  `final_exam` int(100) NOT NULL," #50
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['COMP2048'] = (
    "CREATE TABLE `COMP2048` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `Demo_1` int(100) NOT NULL," #20
    "  `Demo_2` int(100) NOT NULL," #20
    "  `Demo_3` int(100) NOT NULL," #20
    "  `Demo_4` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #20
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['CSSE1001'] = (
    "CREATE TABLE `CSSE1001` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `online_quiz` int(100) NOT NULL," #12
    "  `assignment_0` int(100) NOT NULL," #1
    "  `assignment_1` int(100) NOT NULL," #10
    "  `assignment_2` int(100) NOT NULL," #15
    "  `assignment_3` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #42
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['CSSE2002'] = (
    "CREATE TABLE `CSSE2002` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `problem_sets` int(100) NOT NULL," #10
    "  `assignment_1` int(100) NOT NULL," #20
    "  `assignment_2` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #50
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['INFS1200'] = (
    "CREATE TABLE `INFS1200` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `ripple` int(100) NOT NULL," #10
    "  `assignment_1` int(100) NOT NULL," #15
    "  `assignment_2` int(100) NOT NULL," #15
    "  `assignment_3` int(100) NOT NULL," #15
    "  `assignment_4` int(100) NOT NULL," #15
    "  `final_exam` int(100) NOT NULL," #30
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['MATH1061'] = (
    "CREATE TABLE `MATH1061` ("
    "  `enrolment_id` int(20) NOT NULL," 
    "  `course_id` varchar(20) NOT NULL,"
    "  `mid_sem_exam` int(100) NOT NULL," #25
    "  `assignment_1` int(100) NOT NULL," #5
    "  `assignment_2` int(100) NOT NULL," #5
    "  `assignment_3` int(100) NOT NULL," #5
    "  `assignment_4` int(100) NOT NULL," #5
    "  `final_exam` int(100) NOT NULL," #55
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['STAT1201'] = (
    "CREATE TABLE `STAT1201` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `online_quizzes` int(100) NOT NULL," #15
    "  `article_review` int(100) NOT NULL," #5
    "  `essay` int(100) NOT NULL," #10
    "  `video` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #50
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['STAT1301'] = (
    "CREATE TABLE `STAT1301` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `online_quizzes` int(100) NOT NULL," #10
    "  `article_review_1` int(100) NOT NULL," #5
    "  `article_review_2` int(100) NOT NULL," #10
    "  `project` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #55
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    TABLES['COMP4500'] = (
    "CREATE TABLE `COMP4500` ("
    "  `enrolment_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `online_quizzes` int(100) NOT NULL," #10
    "  `assignment_1` int(100) NOT NULL," #20
    "  `assignment_2` int(100) NOT NULL," #20
    "  `final_exam` int(100) NOT NULL," #50
    "  `total_assessment_score_percent` int(100) NOT NULL,"
    "   FOREIGN KEY(enrolment_id) REFERENCES Enrolment(enrolment_id), "
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")

    


    return TABLES
