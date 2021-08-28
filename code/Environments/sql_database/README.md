
# HOW TO USE:
1) Install mySQL WorkBench at https://www.mysql.com/products/workbench/
2) Open the program and add a connection
3) Enter the connection details
    - Connection Method: Standard (TCP/IP)
    - Hostname: university-db-deco3801.mysql.database.azure.com
    - Username: gpr_deco3801@university-db-deco3801
    - Password: Abc1234567890
    - Port: 3306
4) Now we can write queries in the window for the database

## install_scripts.py
- installs the necessary packages to run the files

## query.py
- Allows user to write query. 

## database.py
-   Contains the methods of the sql database like create table, inserting the table, and retrieve the data. 

## populate.py
- This file populates the database

## table_lists.py
- Contains the list of tables in our database

## Metrics for measuring student's SATISFACTION:
- We will be using the student's Interaction and Attendance as a measure of satisfaction.
- Rationale: If a student is satisfied with the course, they will pay more attention in class, attend more classes and interact more. 

## Metrics for measuring a student's PERFORMANCE:
- For every enrolment, we assume that every course has 4 topics for consistency and simplicity purposes. (NOTE: 1 enrolment_id per course).
- For every enrolment/course, we will measure the performance of:
    - The 4 topics.
    - The attendance.
    - The Interaction
    - The assessments
    - GPA, calculated based on the average of the above 4 categories. 

## Metrics for measuring COURSE EFFECTIVENESS:
- Effectiveness will be measured based on real world application. If there is high real world
application, then this would mean the course has higher effectiveness. 