# Machine learning
## HOW TO USE:
1) Go to main() and insert the name of the file in the string
2) Make sure to uncomment which prediction, e.g. uncomment read_file_satisfaction(file_to_predict) if predicting satisfaction of student
3) Make sure the CSV file to predict is in the 'predict' folder. 


## Predict grade
To predict the grade, we need the following information:
- All 4 topic %
- Attendance %
- Interaction %
To simplify the prediction, the model will take in the total % of each category (except for the topics). 

Goal: To predict a gpa (1 to 7) for a student based on the provided information above. 


## Predict Satisfaction
To predict the satisfaction, we will use:
- Attendance %
- Interaction %
- Survey rating %

Goal: To predict if a student is satisfied or is not satisfied with the course with the provided information above. 

We will use SVM(Support Vector Machine) as our machine learning model as it supports binary classification. In our case, we have binary classifications of 0 (for unsatisfied) and 1 (for satisfied). 

## Generated Data
- The data in the CSV files each have 17,560 entries (enrolments).