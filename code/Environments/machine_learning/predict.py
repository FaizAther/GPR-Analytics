import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def read_file_satisfaction(name):
    file = '../GPR-Analytics/code/Environments/machine_learning/data/raw_data/data_satisfaction.csv'
    predict_file = '../GPR-Analytics/code/Environments/machine_learning/data/predict/%s.csv' %(name)
    data = pd.read_csv(file) 
    to_predict = pd.read_csv(predict_file) 
    return svm_satisfaction(data, to_predict)

def read_file_grade(name):
    file = '../GPR-Analytics/code/Environments/machine_learning/data/raw_data/data_grade.csv'
    predict_file = '../GPR-Analytics/code/Environments/machine_learning/data/predict/%s.csv' %(name)
    data = pd.read_csv(file) 
    to_predict = pd.read_csv(predict_file) 
    return svm_grade(data, to_predict)

def svm_satisfaction(data, to_predict):
    """
    This function uses 80% of the data for training and 20% for testing to provide the
    accuracy report. 
    """
    X = data.iloc[:,:-1] # get all columns except last one
    y = data.iloc[: , -1] # get last column

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    predict = svclassifier.predict(to_predict)
    print("----- Prediction -----")
    print("Accuracy of prediction: %s%%" %((accuracy_score(y_test, y_pred)*100)))
    for i in range(len(predict)):
        print("Entry %s: %s" %(i, predict[i]))
    return predict

def svm_grade(data, to_predict):
    return

def main():
    # comment out whichever you dont want to predict
    file_to_predict = "test_predict_satisfaction" # type in the name of file

    # predict the satisfaction
    read_file_satisfaction(file_to_predict)
    
    # predict the grade
    # read_file_grade(file_to_predict)

if __name__ == "__main__":
    main()