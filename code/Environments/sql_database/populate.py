# from pip._internal import main
# main(['install','names'])
import random
import names

n = 1000 # number of students to generate
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

def pop_enrolment(student_id_list, course_id_list, performance_id_list):
    # enrolment entry for table: [student_id, course_id, enrol_date, study_type, performance_id]
    list = []
    type = ["Full-time", "Part-time"]
    enrolment_dates = ["2021-01-29", "2021-07-16", "2021-11-12"] # sem1, sem2, summer sem (2021)
    id_list = random.sample(range(5000000, 9999999), n)
    for i in range(n):
        enrolment_id = id_list[i]
        student_id = student_id_list[i][0]
        course_id = course_id_list[i][0]
        enrol_date = random.choice(enrolment_dates)
        study_type = random.choice(type)
        performance_id = performance_id_list[i][0]

        entry = (enrolment_id,student_id, course_id, enrol_date, study_type, performance_id)
        list.append(entry)
    return list

def pop_performance(course_id_list):
    # enrolment entry for table: 
    # [
    # performance_id, course_id, lecture_attendance, tutorial_attendance,
    # practical_attendance, personal_study, mid_sem_exam, quiz_score,
    # assignment_score, total_assessment_score, grade, at_risk]
    list = []
    id_list = random.sample(range(100000, 500000), n)
    for i in range(n):
        performance_id = id_list[i]
        course_id = random.choice(course_id_list)

        mid_sem_exam = random.sample(range(0, 100), 1)
        quiz_score = random.sample(range(0, 100), 1)
        assignment_score = random.sample(range(0, 100), 1)
        total_assessment_score = (mid_sem_exam[0] + quiz_score[0] + assignment_score[0]) / 3

        # determine the gpa
        if total_assessment_score < 20:
            grade = 1
            lecture_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            personal_study = random.sample(range(0, int(total_assessment_score)), 1)

        if total_assessment_score >= 20 and total_assessment_score < 45:
            grade = 2
            lecture_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            personal_study = random.sample(range(0, int(total_assessment_score)), 1)

        if total_assessment_score >= 45 and total_assessment_score < 50:
            grade = 3
            lecture_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(0, int(total_assessment_score)), 1)
            personal_study = random.sample(range(0, int(total_assessment_score)), 1)

        if total_assessment_score >= 50 and total_assessment_score < 65:
            grade = 4
            lecture_attendance = random.sample(range(49, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(49, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(49, int(total_assessment_score)), 1)
            personal_study = random.sample(range(49, int(total_assessment_score)), 1)

        if total_assessment_score >= 65 and total_assessment_score < 75:
            grade = 5
            lecture_attendance = random.sample(range(64, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(64, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(64, int(total_assessment_score)), 1)
            personal_study = random.sample(range(64, int(total_assessment_score)), 1)

        if total_assessment_score >= 75 and total_assessment_score < 85:
            grade = 6
            lecture_attendance = random.sample(range(74, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(74, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(74, int(total_assessment_score)), 1)
            personal_study = random.sample(range(74, int(total_assessment_score)), 1)

        if total_assessment_score >= 85:
            grade = 7
            lecture_attendance = random.sample(range(84, int(total_assessment_score)), 1)
            tutorial_attendance = random.sample(range(84, int(total_assessment_score)), 1)
            practical_attendance = random.sample(range(84, int(total_assessment_score)), 1)
            personal_study = random.sample(range(84, int(total_assessment_score)), 1)

        if grade <= 3:
            at_risk = 1 # 0 is false, 1 is true
        if grade > 3:
            at_risk = 0

        entry = (performance_id, course_id[0], lecture_attendance[0], tutorial_attendance[0],
                practical_attendance[0], personal_study[0], mid_sem_exam[0], quiz_score[0],
                assignment_score[0], total_assessment_score, grade, at_risk)
        list.append(entry)
    return list

