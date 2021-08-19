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
    TABLES['student'] = (
    "CREATE TABLE `student` ("
    "  `student_id` int(20) NOT NULL AUTO_INCREMENT,"
    "  `age` int(10) NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `degree` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")

    TABLES['course'] = (
    "CREATE TABLE `course` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `course_name` varchar(14) NOT NULL,"
    "  `year` int(14) NOT NULL,"
    "  PRIMARY KEY (`course_id`)"
    ") ENGINE=InnoDB")

    TABLES['enrolments'] = (
    "CREATE TABLE `enrolments` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `student_id` varchar(14) NOT NULL,"
    "  `enrol_date` date NOT NULL"
    # "  PRIMARY KEY (`enrolment_id`)"
    ") ENGINE=InnoDB")

    TABLES['grades'] = (
    "CREATE TABLE `grades` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `student_id` varchar(14) NOT NULL,"
    "  `year` int(4) NOT NULL,"
    "  `semester` int(1) NOT NULL,"
    "  `grade` int(100) NOT NULL"
    # "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")
    
    TABLES['course_info'] = (
    "CREATE TABLE `course_info` ("
    "  `course_id` varchar(20) NOT NULL,"
    "  `lecturer` varchar(14) NOT NULL"
    # "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")

    ### TODO ###
    # fix the primary and foreign keys


    return TABLES
