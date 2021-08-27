
# HOW TO USE:
## query.py
    - Allows user to write query. 
    - Make sure to have installed 'mysql-connector-python' package. 
        - Try 'pip install mysql-connector-python'

## database.py
    -   Make sure to have installed 'mysql-connector-python' package. 
        - Either 'pip install mysql-connector-python' or uncomment top code block
    -   Contains the methods of the sql database like create table, inserting the table, and retrieve the data. 

## populate.py
This file populates the database

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