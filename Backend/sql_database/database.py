
import mysql.connector
from mysql.connector import errorcode

from table_lists import tables
import populate

# establish the connection to azure sql database
db = "university_db"

cnx = mysql.connector.connect(
    host="university-db-deco3801.mysql.database.azure.com",
    user="deco3801_login@university-db-deco3801",
    passwd="Abcd1234",
    database=db
)
# mycursor.execute("CREATE DATABASE university_db")


mycursor = cnx.cursor()

def show_databases():
    '''
    Show list of databases in the system
    '''
    mycursor.execute("SHOW DATABASES")
    for database in mycursor:
        print(database)


def show_tables():
    '''
    Show list of tables in the database
    '''
    mycursor.execute("SHOW TABLES")
    for table in mycursor:
        print(table)

def create_tables(DB_NAME, cursor, TABLES):
    '''
    Create tables from the import list
    '''
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_tables(DB_NAME, cursor, TABLES)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()

def insert_student():
    sql = "INSERT INTO student (student_id, name, age, degree)\
           VALUES (%s,%s,%s,%s)"
    list = populate.pop_student()
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_goals():
    student_id_list = []
    mycursor.execute("SELECT student_id from student")
    result = mycursor.fetchall()
    for row in result:
        student_id_list.append(row)
    
    list = populate.pop_goals(student_id_list)
    sql = "INSERT INTO goals (student_id, gpa, lec_attendance, tut_attendance)\
           VALUES (%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_course():
    sql = "INSERT INTO course (course_id, name, level)\
           VALUES (%s,%s,%s)"
    list = populate.pop_course()
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def query_data(string):
    save_query = []
    mycursor.execute(string)
    result = mycursor.fetchall()
    for row in result:
        print(row)
        save_query.append(row)
    return save_query

def insert_enrolment():
    # we need to get student_id from student table
    student_id_list = []
    mycursor.execute("SELECT student_id from student")
    result = mycursor.fetchall()
    for row in result:
        student_id_list.append(row)

    # we need to get course_id from Performance table
    course_id_list = []
    mycursor.execute("SELECT course_id from course")
    result = mycursor.fetchall()
    for row in result:
        course_id_list.append(row)

    list = populate.pop_enrolment(student_id_list, course_id_list)
    sql = "INSERT INTO enrolment (enrolment_id, student_id, course_id, enrol_date, study_type)\
            VALUES (%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_statistic():
    # we need to get course_id
    save_query = []
    mycursor.execute("SELECT course_id from course")
    result = mycursor.fetchall()
    for row in result:
        save_query.append(row)
    
    list = populate.pop_course_statistic(save_query)
    sql = "INSERT INTO course_statistic (course_id, pass_rate_percent, drop_out_percent, real_world_app_percent, effectiveness_percent)\
            VALUES (%s,%s,%s,%s, %s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_attendance():
    save_query = []
    mycursor.execute("SELECT enrolment_id from enrolment")
    result = mycursor.fetchall()
    for row in result:
        save_query.append(row)
    
    list = populate.pop_attendance(save_query)
    sql = "INSERT INTO attendance (enrolment_id, lec_attendance_percent, tut_attendance_percent, lec_incompletion_percent, tut_incompletion_percent, total_attendance_percent)\
            VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return
    
def insert_grade():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)
    
    courses = set()
    for i in range(len(enrol_query)):
        courses.add(enrol_query[i][2])

    # get all the courses
    course_query = []
    for c in courses:
        mycursor.execute("SELECT * from %s" % (c))
        result = mycursor.fetchall()
        for row in result:
            course_query.append(row)

    
    list = populate.pop_grade(enrol_query, course_query)
    sql = "INSERT INTO grade (enrolment_id, gpa, at_risk)\
            VALUES (%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_satisfaction():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    att_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        att_query.append(row)
    
    list = populate.pop_satisfaction(enrol_query, att_query)
    sql = "INSERT INTO satisfaction (enrolment_id, satisfaction_rate_percent, mid_sem_survey_rating_percent, final_survey_rating_percent, is_satisfied)\
            VALUES (%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_CSSE2010():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_CSSE2010(enrol_query, attend_query)
    sql = "INSERT INTO CSSE2010 (enrolment_id, course_id, weekly_quiz, assignment_1, assignment_2, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_COMP3506():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_COMP3506(enrol_query, attend_query)
    sql = "INSERT INTO COMP3506 (enrolment_id, course_id, weekly_quiz, Project, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_COMP2048():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_COMP2048(enrol_query, attend_query)
    sql = "INSERT INTO COMP2048 (enrolment_id, course_id, Demo_1, Demo_2, Demo_3, Demo_4, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_CSSE1001():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_CSSE1001(enrol_query, attend_query)
    sql = "INSERT INTO CSSE1001 (enrolment_id, course_id, online_quiz, assignment_0, assignment_1, assignment_2, assignment_3, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_CSSE2002():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_CSSE2002(enrol_query, attend_query)
    sql = "INSERT INTO CSSE2002 (enrolment_id, course_id, problem_sets, assignment_1, assignment_2, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_INFS1200():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_INFS1200(enrol_query, attend_query)
    sql = "INSERT INTO INFS1200 (enrolment_id, course_id, ripple, assignment_1, assignment_2,assignment_3, assignment_4, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_MATH1061():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_MATH1061(enrol_query, attend_query)
    sql = "INSERT INTO MATH1061 (enrolment_id, course_id, mid_sem_exam, assignment_1, assignment_2, assignment_3, assignment_4, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_STAT1201():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_STAT1201(enrol_query, attend_query)
    sql = "INSERT INTO STAT1201 (enrolment_id, course_id, online_quizzes, article_review, essay, video, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_STAT1301():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_STAT1301(enrol_query, attend_query)
    sql = "INSERT INTO STAT1301 (enrolment_id, course_id, online_quizzes, article_review_1, article_review_2, project, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return
    
def insert_COMP4500():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    list = populate.pop_COMP4500(enrol_query, attend_query)
    sql = "INSERT INTO COMP4500 (enrolment_id, course_id, online_quizzes, assignment_1, assignment_2, final_exam, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return


def main():
    '''
    Can only execute one function because cursor can only execute 1 time.
    Comment out other functions to use the function you want.

    Mainly use this part for populating the database.
    '''
    # create_tables(db, mycursor, tables()) # create tables
    # insert_student()
    # insert_goals()
    # insert_course()
    # insert_statistic()
    # insert_enrolment()
    # insert_attendance()
    # insert_satisfaction()

    # insert_CSSE2010()
    # insert_COMP2048()
    # insert_COMP3506()
    # insert_CSSE1001()
    # insert_CSSE2002()
    # insert_INFS1200()
    # insert_MATH1061()
    # insert_STAT1201()
    # insert_STAT1301()
    # insert_COMP4500()

    # insert_grade()
    


if __name__=="__main__":
    main()

