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
    course_id = ["COMP2048","COMP3506","CSSE1001","CSSE2002","CSSE2010","INFS1200","MATH1061","STAT1201","STAT1301","COMP4500"]
    name = ["Theory of Computing", "Algorithms & Data Structure", "Introduction to Software Engineering",
        "Programming in the Large", "Introduction to Computer Systems", "Introduction to Information Systems",
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

def pop_satisfaction(enrolment_id_list, attendance_list):
    """
    Depend on the surveys
    """
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        total_attendance = attendance_list[i][5]
        min_survey = (total_attendance) / 2 # lower bound
        mid_survey = random.randint(int(min_survey), 100)
        final_survey = random.randint(int(min_survey), 100)
        satisfaction_rate = (mid_survey + final_survey) / 2

        if int(satisfaction_rate) >= 50:
            # satisfied
            is_satisfied = 1
        if int(satisfaction_rate) < 50:
            # not satisfied
            is_satisfied = 0

        entry = (enrolment_id_list[i][0], int(satisfaction_rate), mid_survey, final_survey, is_satisfied)
        list.append(entry)
    return list

def pop_grade(enrolment_id_list, course_list):
    list = []
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    course = sorted(course_list)

    for i in range(len(enrolments)):
        enrol_id = enrolments[i][0]
        last = len(course[i]) - 1
        total_assessment_score = course[i][last]
        
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

        entry = (enrol_id, grade, at_risk)
        list.append(entry)

    return list

def pop_attendance(enrolment_id_list):
    list = []
    num = len(enrolment_id_list)
    for i in range(num):
        lec_attendance = random.randint(0, 100)
        tut_attendance = random.randint(0, 100)
        lec_incompletion = random.randint(0, 100)
        tut_incompletion = random.randint(0, 100)
        total_attendance = (lec_attendance + tut_attendance + lec_incompletion + tut_incompletion) /5

        entry = (enrolment_id_list[i][0], 
                lec_attendance,tut_attendance,
                lec_incompletion,
                tut_incompletion,
                total_attendance)
        list.append(entry)

    return list

def pop_CSSE2010(enrolment_id_list, attendance_list):
    list = []
    id = "CSSE2010"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        weekly_quiz = (random.randint(total_attendance, 100) / 100) * 10
        a1 = (random.randint(total_attendance, 100) / 100) * 20
        a2 = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 50
        total = weekly_quiz + a1 + a2 + final

        if course_id == id:
            entry = [enrolment_id, course_id, weekly_quiz, a1, a2, final, total]
            list.append(entry)
    return list

def pop_COMP3506(enrolment_id_list, attendance_list):
    list = []
    id = "COMP3506"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        weekly_quiz = (random.randint(total_attendance, 100) / 100) * 20
        project = (random.randint(total_attendance, 100) / 100) * 30
        final = (random.randint(total_attendance, 100) / 100) * 50
        total = weekly_quiz + project + final

        if course_id == id:
            entry = [enrolment_id, course_id, weekly_quiz, project, final, total]
            list.append(entry)
    return list

def pop_COMP2048(enrolment_id_list, attendance_list):
    list = []
    id = "COMP2048"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        demo_1 = (random.randint(total_attendance, 100) / 100) * 20
        demo_2 = (random.randint(total_attendance, 100) / 100) * 20
        demo_3 = (random.randint(total_attendance, 100) / 100) * 20
        demo_4 = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 20
        total = demo_1 + demo_2 + demo_3 + demo_4 + final

        if course_id == id:
            entry = [enrolment_id, course_id, demo_1, demo_2, demo_3, demo_4, final, total]
            list.append(entry)
    return list

def pop_CSSE1001(enrolment_id_list, attendance_list):
    list = []
    id = "CSSE1001"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        online_quiz = (random.randint(total_attendance, 100) / 100) * 12
        a0 = (random.randint(total_attendance, 100) / 100) * 1
        a1 = (random.randint(total_attendance, 100) / 100) * 10
        a2 = (random.randint(total_attendance, 100) / 100) * 15
        a3 = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 42
        total = online_quiz + a0+ a1 + a2 + a3+ final

        if course_id == id:
            entry = [enrolment_id, course_id, online_quiz, a0, a1, a2, a3, final, total]
            list.append(entry)
    return list

def pop_CSSE2002(enrolment_id_list, attendance_list):
    list = []
    id = "CSSE2002"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        problem_sets = (random.randint(total_attendance, 100) / 100) * 10
        a1 = (random.randint(total_attendance, 100) / 100) * 20
        a2 = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 50
        total = problem_sets + a1 + a2 + final

        if course_id == id:
            entry = [enrolment_id, course_id, problem_sets, a1, a2, final, total]
            list.append(entry)
    return list

def pop_INFS1200(enrolment_id_list, attendance_list):
    list = []
    id = "INFS1200"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        ripple = (random.randint(total_attendance, 100) / 100) * 10
        a1 = (random.randint(total_attendance, 100) / 100) * 15
        a2 = (random.randint(total_attendance, 100) / 100) * 15
        a3 = (random.randint(total_attendance, 100) / 100) * 15
        a4 = (random.randint(total_attendance, 100) / 100) * 15
        final = (random.randint(total_attendance, 100) / 100) * 30
        total = ripple + a1 + a2 + a3 + a4 + final

        if course_id == id:
            entry = [enrolment_id, course_id,ripple,a1,a2,a3,a4,final, total]
            list.append(entry)
    return list

def pop_MATH1061(enrolment_id_list, attendance_list):
    list = []
    id = "MATH1061"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        mid_sem_exam = (random.randint(total_attendance, 100) / 100) * 25
        a1 = (random.randint(total_attendance, 100) / 100) * 5
        a2 = (random.randint(total_attendance, 100) / 100) * 5
        a3 = (random.randint(total_attendance, 100) / 100) * 5
        a4 = (random.randint(total_attendance, 100) / 100) * 5
        final = (random.randint(total_attendance, 100) / 100) * 55
        total = mid_sem_exam + a1 + a2 + a3 + a4 + final

        if course_id == id:
            entry = [enrolment_id, course_id,mid_sem_exam,a1,a2,a3,a4,final, total]
            list.append(entry)
    return list

def pop_STAT1201(enrolment_id_list, attendance_list):
    list = []
    id = "STAT1201"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        online_quizzes = (random.randint(total_attendance, 100) / 100) * 15
        article_review = (random.randint(total_attendance, 100) / 100) * 5
        essay = (random.randint(total_attendance, 100) / 100) * 10
        video = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 50
        total = online_quizzes + article_review + essay + video + final

        if course_id == id:
            entry = [enrolment_id, course_id, online_quizzes, article_review, essay, video, final, total]
            list.append(entry)
    return list

def pop_STAT1301(enrolment_id_list, attendance_list):
    list = []
    id = "STAT1301"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        online_quizzes = (random.randint(total_attendance, 100) / 100) * 10
        article_review_1 = (random.randint(total_attendance, 100) / 100) * 5
        article_review_2 = (random.randint(total_attendance, 100) / 100) * 10
        project = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 55
        total = online_quizzes + article_review_1 + article_review_2 + project + final

        if course_id == id:
            entry = [enrolment_id, course_id, online_quizzes, article_review_1, article_review_2, project, final, total]
            list.append(entry)
    return list

def pop_COMP4500(enrolment_id_list, attendance_list):
    list = []
    id = "COMP4500"
    
    # sort the lists
    enrolments = sorted(enrolment_id_list)
    attendance = sorted(attendance_list)
    
    for i in range(len(enrolment_id_list)):
        enrolment_id = enrolments[i][0]
        course_id = enrolments[i][2]
        # assessments are determined by attendance
        total_attendance = attendance[i][5]
        online_quizzes = (random.randint(total_attendance, 100) / 100) * 10
        a1 = (random.randint(total_attendance, 100) / 100) * 20
        a2 = (random.randint(total_attendance, 100) / 100) * 20
        final = (random.randint(total_attendance, 100) / 100) * 50
        total = online_quizzes + a1 + a2 + final

        if course_id == id:
            entry = [enrolment_id, course_id, online_quizzes, a1, a2, final, total]
            list.append(entry)
    return list