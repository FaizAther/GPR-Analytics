# Azure SQL Database
hostname: university-db-deco3801.mysql.database.azure.com
user: gpr_deco3801@university-db-deco3801
password: Abc1234567890
database: university_db

## database.py
Contains the methods of the sql database like create table, inserting the table, and retrieve the data.

## populate.py
This file populates the database

## query.py
Allows user to write query

## table_lists.py
Contains the list of tables in our database
### Note: Performance table
- at_risk Attribute is a boolean data type (0,1) where 0 is false and 1 is true.
- For example, if we want to find all the students who are 'at risk', we can query:
    - "SELECT * 
        FROM student,enrolment,performance 
        WHERE student.student_id = enrolment.student_id 
        AND enrolment.performance_id = performance.performance_id 
        AND performance.at_risk = '1';"