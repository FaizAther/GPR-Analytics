#### If mysql is not installed, uncomment the code below and install ####
# from pip._internal import main
# main(['install','mysql-connector-python-rf'])

from __future__ import print_function # this line needs to be first, make sure to comment out above
import mysql.connector
from mysql.connector import errorcode

from table_lists import tables
from populate import pop_student, pop_course

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

def insert_student(list):
    sql = "INSERT INTO student (student_id, name, age, degree)\
           VALUES (%s,%s,%s,%s)"
    mycursor.executemany(sql, list)
    cnx.commit()
    return

def insert_course(list):
    sql = "INSERT INTO course (course_id, name, level)\
           VALUES (%s,%s,%s)"
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
    
def main():
    '''
    Can only execute one function because cursor can only execute 1 time.
    Comment out other functions to use the function you want.

    Mainly use this part for populating the database.
    '''
    #create_tables(db, mycursor, tables()) # create tables
    # show_tables()
    #insert_student(pop_student())
    #insert_course(pop_course())


if __name__=="__main__":
    main()

