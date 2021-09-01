import random
import names

n = 5000 # number of students to generate
def pop_student():
    list = []
    # student format: (student_id, name, age, degree)
    degrees = [
        'Bachelor of Computer Science',
        'Bachelor of Architectural Design',
        'Bachelor of Information Technology',
        'Bachelor of Engineering',
        'Bachelor of Design',
        'Bachelor of Commerce',
        'Bachelor of Economics',
        'Bachelor of Arts',
        'Bachelor of Business Management',
        'Bachelor of Mathematics',
        'Bachelor of Laws'
    ]
    id_list = random.sample(range(40000000, 49999999), n)
    
    for i in range(n):
        student_id = id_list[i]
        name = (names.get_full_name())
        age = random.sample(range(18, 60), 1)
        degree = random.choice(degrees)
        list.append((student_id, name, age[0], degree))
    return list

def pop_goals(student_id):
    list = []
    i = 0
    while i < n:
        gpa = random.sample(range(4, 7), 1)
        lec = random.sample(range(50, 100), 1)
        tut = random.sample(range(50, 100), 1)

        entry = (student_id[i][0], gpa[0], lec[0], tut[0])
        list.append(entry)
        i += 1

    return list

def pop_course():
    # course entry for table: [course_id, name, level]
    list = []
    course_id = ["COMP2048","COMP3506","CSSE1001","CSSE2002","COMP2010","INFS1200","MATH1061","STAT1201","STAT1301","COMP4500"]
    name = ["Theory of Computing", "Algorithms & Data Structure", "Introduction to Software Engineering",
        "Programming in the Large", "Introductino to Computer Systems", "Introduction to Information Systems",
        "Discrete Mathematics", "Analysis of Scientific Data", "Advanced Analysis of Scientific Data", "Advanced Algorithms & Data Structure"]

    i = 0
    while i < len(name):
        entry = (course_id[i], name[i], "Undergraduate")
        list.append(entry)
        i += 1

    return list

def pop_enrolment(student_id_list, course_id_list):
    # enrolment entry for table: [student_id, course_id, enrol_date, study_type, performance_id]
    list = []
    type = ["Full-time", "Part-time"]
    enrolment_dates = ["2021-01-29", "2021-07-16", "2021-11-12"] # sem1, sem2, summer sem (2021)
    id_list = random.sample(range(5000000, 9999999), n * 5) # enrolment id
    for i in range(n):
        # each student enrols into 3-4 courses
        study_type = random.choice(type)
        if study_type == "Full-time":
            course_ids = random.sample(course_id_list, 4)
            for j in range(4):
                enrolment_id = id_list.pop(-1)
                student_id = student_id_list[i][0]
                course_id = course_ids[j]
                enrol_date = random.choice(enrolment_dates)
                entry = (enrolment_id,student_id, course_id[0], enrol_date, study_type)
                list.append(entry)

        elif study_type == "Part-time":
            course_ids = random.sample(course_id_list, 3)
            for j in range(3):
                enrolment_id = id_list.pop(-1)
                student_id = student_id_list[i][0]
                course_id = course_ids[j]
                enrol_date = random.choice(enrolment_dates)
                entry = (enrolment_id,student_id, course_id[0], enrol_date, study_type)
                list.append(entry)
    return list

def pop_topics(enrolment_id_list):
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        topic_one = random.sample(range(0, 100), 1)
        topic_two = random.sample(range(0, 100), 1)
        topic_three = random.sample(range(0, 100), 1)
        topic_four = random.sample(range(0, 100), 1)

        entry = (enrolment_id_list[i][0], topic_one[0], topic_two[0], topic_three[0], topic_four[0])
        list.append(entry)
    return list

def pop_course_statistic(course_id_list):
    list = []
    num = len(course_id_list)
    for i in range(num):
        pass_rate = random.randint(50, 100)
        drop_out_rate = random.randint(0, 100 - pass_rate)
        real_world_app = random.randint(40, 100)
        effectiveness = random.randint(real_world_app, 100)

        entry = (course_id_list[i][0], pass_rate, drop_out_rate, real_world_app, effectiveness)
        list.append(entry)
    return list

def pop_satisfaction(enrolment_id_list, interaction_list, attendance_list):
    """
    Depend on the attendance and interaction
    """
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        total_interaction = interaction_list[i][3] 
        total_attendance = attendance_list[i][6]
        min_survey = (total_attendance + total_interaction) / 2
        survey_rating = random.randint(int(min_survey), 100)
        satisfaction_rate = (total_attendance +total_attendance + survey_rating) / 3

        if int(satisfaction_rate) >= 50:
            is_satisfied = 1
        if int(satisfaction_rate) < 50:
            is_satisfied = 0

        entry = (enrolment_id_list[i][0], int(satisfaction_rate), survey_rating, is_satisfied)
        list.append(entry)
    return list

def pop_interaction(enrolment_id_list):
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        lec_interaction= random.randint(0, 100)
        tut_interaction = random.randint(0, 100)
        total_interaction = (lec_interaction + tut_interaction) / 2

        entry = (enrolment_id_list[i][0], lec_interaction, tut_interaction, total_interaction)
        list.append(entry)

    return list

def pop_grade(enrolment_id_list,assessment_list):
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        total_assessment_score = assessment_list[i][4]
        # determine the gpa
        if total_assessment_score < 20:
            grade = 1
        if total_assessment_score >= 20 and total_assessment_score < 45:
            grade = 2
        if total_assessment_score >= 45 and total_assessment_score < 50:
            grade = 3
        if total_assessment_score >= 50 and total_assessment_score < 65:
            grade = 4
        if total_assessment_score >= 65 and total_assessment_score < 75:
            grade = 5
        if total_assessment_score >= 75 and total_assessment_score < 85:
            grade = 6
        if total_assessment_score >= 85:
            grade = 7
        
        if grade <= 3:
            at_risk = 1 # 0 is false, 1 is true
        if grade > 3:
            at_risk = 0

        entry = (assessment_list[i][0], grade, at_risk)
        list.append(entry)

    return list

def pop_assessment(enrolment_id_list, attendance_list, interaction_list, topics_list):
    """
    The idea of measuring the assessment is if the attendance, interaction and topics are
    high, then the assessment marks should be high (average). 
    """
    list = []
    num = len(enrolment_id_list)
    
    for i in range(num):
        total_attendance = attendance_list[i][6]
        total_interaction = interaction_list[i][3]
        avg_topics = (topics_list[i][1] + topics_list[i][2] + topics_list[i][3] + topics_list[i][4])/4
        minimum_range = (total_attendance + total_interaction + avg_topics) / 3

        mid_sem = random.randint(int(minimum_range) - 5, int(minimum_range) + 5)
        quiz = random.randint(int(minimum_range) - 5, int(minimum_range) + 5)
        assignment = random.randint(int(minimum_range) - 5, int(minimum_range) + 5)
        total_assessment = (mid_sem + quiz + assignment) / 3

        entry = (enrolment_id_list[i][0], mid_sem, quiz, assignment, total_assessment)
        list.append(entry)
    return list

def pop_attendance(enrolment_id_list):
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        lec_attendance = random.randint(0, 100)
        tut_attendance = random.randint(0, 100)
        personal_study = random.randint(0, 100)
        lec_incompletion = random.randint(0, 100)
        tut_incompletion = random.randint(0, 100)
        total_attendance = (lec_attendance + tut_attendance + personal_study + lec_incompletion + tut_incompletion) /5

        entry = (enrolment_id_list[i][0], 
                lec_attendance,tut_attendance,
                personal_study,
                lec_incompletion,
                tut_incompletion,
                total_attendance)
        list.append(entry)

    return list
