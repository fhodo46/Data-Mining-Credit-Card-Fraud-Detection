# -*- coding: utf-8 -*-
"""Data Mining Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-jy-cmlR0KS0z3UQU0zQ-Q1uTyDEX3rG
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

creditcarddata= pd.read_csv('/content/creditcard.csv')   #reading the csv filepath after the filepath has been copied from the dataset file
creditcarddata.head()  #showing the first 5 rows of the dataset to have an idea of what it is like
#columns from v1 to v2 show only numerical input variables which are the result of a PCA transformation.
#Unfortunately, due to confidentiality issues, the original features and more background information about the data cannot be provided.
#Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'.
#The "Time" column shows the elapsed time (in seconds) from the row n (n+1th transaction) to row 0 (first transaction)
#The "Amount" column shows the amount of transaction in dollars

creditcarddata.tail() #showing the last 5 rows of the dataset; there are 284807 transactions in total (284806+1)

creditcarddata.info() #showing the information of the dataset in a tabular chart, like below

creditcarddata['Class'].value_counts() #this counts the number of fraudulent and non-fraudulent transactions (denoted by 1 and 0, respectively).

legitstatus0= creditcarddata[creditcarddata.Class==0] #Separating the data as legit or fraudulent according to the class status
fraudulentstatus1= creditcarddata[creditcarddata.Class==1]
print(legitstatus0.shape)     #Keeping the frequency of rows that have fraudulent data (with status 1) and those that have legit data (with status 0)
#in a tuple, together with the number of columns
print(fraudulentstatus1.shape)

legitstatus0.Amount.describe() #this gives statistical information about the columns that have a status 0 (non-fraudulent transaction)

fraudulentstatus1.Amount.describe() #this gives statistical information about the columns that have a status 1 (fraudulent transaction)

creditcarddata.groupby('Class').mean()  #this gives a comparison about the average data of the columns that have a status 0 (non-fraudulent transaction) and a status 1 (fraudulent).

legitsample= legitstatus0.sample(n=492)  #We saw that there was an uneven number of 0's and 1's, and this will cause errors during the prediction of the fraud
#because there were 99% 0's and 1% 1's; the system will think that there is a 99% chance of a transaction that is not fraudulent and 1% not. We use a
#technique, the under-sampling, which means that we choose the number of columns that are even (that have a status) and we make the statuses 0 and 1 have equal number of columns.
#This is made to have a better accuracy of classification and prediction models of fraud detection in the dataset

newdataset= pd.concat([legitsample,fraudulentstatus1], axis=0) #axis-0 means row-wise; we concat the data from the rows of the columns that have the status 1 and those
#that have a status 0 (fraudulent/non-fraudulent). The rows will be shuffled randomly, which means that we will have rows with status 0 and rows with status 1 mixed up.
#Since 99% of the rows have status 0, it is very unlikely that a row with status 1 will come up.

newdataset.head()

newdataset.tail()

newdataset['Class'].value_counts()   #We see that we have an equal number of 0's and 1's now (in terms of the rows)

newdataset.groupby('Class').mean() #We compare the mean of these rows of 0's and 1's now to see if they have same or different values than before. It seems that the values are
#nearly the same, so it means that the dataset's nature has not changed

x= newdataset.drop(columns='Class', axis=1)  #The data will be displayed column-wise (axis=1), without the data from the column "Class" (which is only the status of transaction)
#and does not give any information to the general type of data other than being fraudulent or non-fraudulent.

print(x)

print(y)

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, stratify=y, random_state=2) #without stratify, 0 and 1 can be very different in the training and testing data
print(x.shape, x_train.shape, x_test.shape) #We divide the collected data into the training and testing data. Features are passed on the x variable, whereas the labels (classes)
#on the y variable. The test size will cover only 20% of the total columns (984 now, since there are 492 columns with class 0 and 492 with class 1), so there will be
#197 columns (which are shown by the x_test.shape). The training part will have 787 other columns and the total of them will result in the 984 columns.

"""Model Training; Logistic Regression"""

model=LogisticRegression()
model.fit(x_train, y_train) #training the logistic regression model with training data from both features/data (x_train) and labels/classes (y_train)

x_train_prediction= model.predict(x_train)  #predicting the model with feature data and then generating the accuracy score of both the predicted model with feature data
#plus the label data
trainingdataaccuracy= accuracy_score(x_train_prediction, y_train)

print('Training data accuracy: ', trainingdataaccuracy)  #The model works correctly only if the training data accuracy score is the same as the testing data one.
#Otherwise, it may be problematic.

x_test_prediction= model.predict(x_test) #a similar procedure but now with test data
testdataaccuracy= accuracy_score(x_test_prediction, y_test)

print('Test data accuracy: ', testdataaccuracy)