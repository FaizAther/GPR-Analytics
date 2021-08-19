def tables():
    TABLES = {}
    TABLES['student'] = (
    "CREATE TABLE `student` ("
    "  `student_id` int(20) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB")
    
    ### TODO ###
    # MAKE MORE TABLES



    return TABLES
