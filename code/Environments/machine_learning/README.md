# Machine learning
## HOW TO USE:
1) Go to main() and insert the name of the file in the string
2) Make sure to uncomment which prediction, e.g. uncomment read_file_satisfaction(file_to_predict) if predicting satisfaction of student
3) Make sure the CSV file to predict is in the 'predict' folder. 


## Predict grade
To predict the grade, we need the following information (ORDER MATTERS):
- Interaction %
- Attendance %
- All 4 topic % (topic_1 %, topic_2 %, topic_3 %,topic_4 %)
- Total_assessment_score %

Example entry: 
[(Interaction %, Attendance %, topic_1 %, topic_2 %, topic_3 %,topic_4 %, Total_assessment_score %)] = [(34,66,10,43,22,93,45)]

To simplify the prediction, the model will take in the total % of each category (except for the topics). 

Goal: To predict a gpa (1 to 7) for a student based on the provided information above. 

We will use KNearest Neighbour to predict the GPA as the model is useful for multi-class classification.

## Predict Satisfaction
To predict the satisfaction, we need the following information (ORDER MATTERS):
- Interaction %
- Attendance %
- Survey rating %
- Satisfaction_rate %

Example prediction entry: [(Interaction %, Attendance %, Survey rating %, Satisfaction_rate %)] = [(20,44,57,40.3)]

Goal: To predict if a student is satisfied or is not satisfied with the course with the provided information above. 

We will use SVM(Support Vector Machine) as our machine learning model as it supports binary classification natively. In our case, we have binary classifications of 0 (for unsatisfied) and 1 (for satisfied). 

## Generated Data
- The data in the CSV files each have 17,523 entries (enrolments).