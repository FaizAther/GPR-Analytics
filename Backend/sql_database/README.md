
# HOW TO USE:
1) Install mySQL WorkBench at https://www.mysql.com/products/workbench/
2) Open the program and add a connection
3) Enter the connection details
    #### THIS PART NEEDS TO BE CHANGED (24/SEPT) ####
    - Connection Method: Standard (TCP/IP)
    - Hostname: university-db-deco3801.mysql.database.azure.com
    - Username: gpr_deco3801@university-db-deco3801
    - Password: Abc1234567890
    - Port: 3306
4) Now we can write queries in the window for the database. Make sure to add "USE university_db;" before writing queuries. 

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
- We will be using the student's mid-semester and final semester surveys to measure a student's satisfaction.
- We don't really need ML to make predictions on surveys as we are determining satisfaction on the total 
rate (< 50% is unsatisfied, >= 50 is satisfied). 
- Rationale: There isn't any other effective methods for measuring a student's satisfaction besides survey

## Metrics for measuring a student's PERFORMANCE:
- It was determined that ML is an overkill for predicting student's performance.
- We will create scatter plots of all assessments for each course and produce a line of best fit to 'predict' a student's GPA. 

## Metrics for measuring COURSE EFFECTIVENESS:
- Effectiveness will be measured based on real world application. If there is high real world
application, then this would mean the course has higher effectiveness. 
- Real-world application % and effectiveness % will just be dummy numbers because it is difficult to obtain those numbers. This data is not important in our application. 