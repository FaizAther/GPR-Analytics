import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file_grade(name):
    file = "../Environments/predict_grade/data/%s.csv" %(name)
    data = pd.read_csv(file)
    if name == "CSSE2010": 
        return grade(data)

def grade(data):
    X = data.iloc[:,2:-1] # get all columns except first and last one

    X.plot()  # plots all columns against index
    X.plot(kind='scatter',x='weekly_quiz') # scatter plot
    X.plot(kind='density')  # estimate density function
    # df.plot(kind='hist')  # histogram


def main():
    # predict the grade
    file_to_predict = "CSSE2010" 
    read_file_grade(file_to_predict)

if __name__ == "__main__":
    main()