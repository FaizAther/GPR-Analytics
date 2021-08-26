def tables():
    '''
    TABLE CREATION FORMAT:
    TABLE['NAME'] = (
    "CREATE TABLE 'NAME' ("
    "  'column name' type() 'condition', "
            ...
            ...
            ...
    ")ENGINE=InnoDB")
    '''

    TABLES = {}
    TABLES['Student'] = (
    "CREATE TABLE `Student` ("
    "  `student_id` int(20) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(100) NOT NULL,"
    "  `age` int(10) NOT NULL,"
    "  `degree` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")

    TABLES['Enrolment'] = (
    "CREATE TABLE `Enrolment` ("
    "  `student_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `enrol_date` date NOT NULL,"
    "  `study_type` varchar(20) NOT NULL,"
    "  `performance_id` int(20) NOT NULL,"
    "   FOREIGN KEY(student_id) REFERENCES Student(student_id),"
    "   FOREIGN KEY(course_id) REFERENCES Course(course_id),"
    "   FOREIGN KEY(performance_id) REFERENCES Performance(performance_id)"
    ") ENGINE=InnoDB")

    TABLES['Course'] = (
    "CREATE TABLE `Course` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `name` varchar(50) NOT NULL,"
    "  `level` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`course_id`)"
    ") ENGINE=InnoDB")

    TABLES['Performance'] = (
    "CREATE TABLE `Performance` ("
    "  `performance_id` int(20) NOT NULL,"
    "  `course_id` varchar(20) NOT NULL,"
    "  `lecture_attendance (%)` int(100) NOT NULL,"
    "  `tutorial_attendance (%)` int(100) NOT NULL,"
    "  `practical_attendance (%)` int(100) NOT NULL,"
    "  `personal_study (%)` int(100) NOT NULL,"
    "  `mid_sem_exam (%)` int(100) NOT NULL,"
    "  `quiz_score (%)` int(100) NOT NULL,"
    "  `assignment_score (%)` int(100) NOT NULL,"
    "  `total_assessment_score (%)` int(100) NOT NULL,"
    "  `grade` int(100) NOT NULL,"
    "  `at_risk` BOOLEAN NOT NULL,"
    "  PRIMARY KEY (`performance_id`),"
    "  FOREIGN KEY(course_id) REFERENCES Course(course_id)"
    ") ENGINE=InnoDB")


    return TABLES
