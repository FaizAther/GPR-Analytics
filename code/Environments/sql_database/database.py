
import mysql.connector
from mysql.connector import errorcode

from table_lists import tables
import populate

# establish the connection to azure sql database
db = "university_db"
cnx = mysql.connector.connect(
    host="university-db-deco3801.mysql.database.azure.com",
    user="gpr_deco3801@university-db-deco3801",
    passwd="Abc1234567890",
    database=db
)
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

def insert_topics():
    # we need to get enrolment_id
    save_query = []
    mycursor.execute("SELECT enrolment_id from enrolment")
    result = mycursor.fetchall()
    for row in result:
        save_query.append(row)
    
    list = populate.pop_topics(save_query)
    sql = "INSERT INTO topics (enrolment_id, topic_one_percent, topic_two_percent, topic_three_percent, topic_four_percent)\
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
    sql = "INSERT INTO attendance (enrolment_id, lec_attendance_percent, tut_attendance_percent, personal_study_percent, lec_incompletion_percent, tut_incompletion_percent, total_attendance_percent)\
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_interaction():
    save_query = []
    mycursor.execute("SELECT enrolment_id from enrolment")
    result = mycursor.fetchall()
    for row in result:
        save_query.append(row)
    
    list = populate.pop_interaction(save_query)
    sql = "INSERT INTO interaction (enrolment_id, lec_interaction_percent, tut_interaction_percent, total_interaction_percent)\
            VALUES (%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_assessments():
    enrol_query = []
    mycursor.execute("SELECT enrolment_id from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    attend_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        attend_query.append(row)

    interact_query = []
    mycursor.execute("SELECT * from interaction")
    result = mycursor.fetchall()
    for row in result:
        interact_query.append(row)

    topics_query = []
    mycursor.execute("SELECT * from topics")
    result = mycursor.fetchall()
    for row in result:
        topics_query.append(row)

    
    list = populate.pop_assessment(enrol_query, attend_query, interact_query, topics_query)
    sql = "INSERT INTO assessments (enrolment_id, mid_sem_exam_percent, quiz_score_percent, assignment_score_percent, total_assessment_score_percent)\
            VALUES (%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return
    
def insert_grade():
    enrol_query = []
    mycursor.execute("SELECT * from enrolment")
    result = mycursor.fetchall()
    for row in result:
        enrol_query.append(row)

    ass_query = []
    mycursor.execute("SELECT * from assessments")
    result = mycursor.fetchall()
    for row in result:
        ass_query.append(row)

    
    list = populate.pop_grade(enrol_query, ass_query)
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

    inter_query = []
    mycursor.execute("SELECT * from interaction")
    result = mycursor.fetchall()
    for row in result:
        inter_query.append(row)

    att_query = []
    mycursor.execute("SELECT * from attendance")
    result = mycursor.fetchall()
    for row in result:
        att_query.append(row)
    
    list = populate.pop_satisfaction(enrol_query, inter_query, att_query)
    sql = "INSERT INTO satisfaction (enrolment_id, satisfaction_rate_percent, survey_rating_percent, is_satisfied)\
            VALUES (%s,%s,%s,%s)"
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
    # insert_statistic()
    # insert_course()

    # insert_enrolment()
    # insert_topics()
    # insert_attendance()
    # insert_interaction()
    # insert_assessments()
    # insert_grade()
    # insert_satisfaction()


if __name__=="__main__":
    main()

