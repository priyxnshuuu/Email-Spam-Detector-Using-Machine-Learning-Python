# -*- coding: utf-8 -*-
"""SpamMailPredictionUsingMachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mik22fAS8hf7FVzpk-Dv_RHaZBsp94PX

1. Importing library
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer  #convert text --> feature vectors(numeric values)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""2. load Dataset"""

raw_mail_data = pd.read_csv('mail_data.csv')

raw_mail_data.head(10)

"""3. Analyses """

raw_mail_data.info()

#replace the null values with a null string
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data), '')

# checking the number of raws and columns in the dataframe
mail_data.shape

"""4. Lable encoding of categorical column"""

# label spam mail as 0; ham mail as 1
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0

mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

"""spam --> 0

ham  --> 1
"""

mail_data.head(10)

"""5. Defining dependendent and independent variable"""

# x = message
# y = category -->(spam,ham)

x = mail_data['Message']

y = mail_data['Category']

print(x)

print(y)

"""6. split x and y into train and test dataset"""

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""7. Feature extraction"""

# transforming the text data to feature vectors that can be used as input to the Logistic Regression

feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = 'True')

# if any word is repeat again and again it give some score like free, offer, discount and according to socre it put mail into Category of spam and ham
# min_df = 1   --> means if score of that word is less then 1 then we are ignore that word
# stop_word = 'english'   --> words like (is,not,did,ok) is ignore by TfidfVectorizer 
# lowercase = 'Truse'   --> means all the word are converting into lowercase

x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)

# convert y_train and y_test values as integers bcoz we want 0 for spam and 1 for ham

y_train = y_train.astype('int')
y_test = y_test.astype('int')

print(x_train_features)

"""8. Train model

Logistic Regression
"""

model = LogisticRegression()

# training the Logistic Regression  model with training data
model.fit(x_train_features, y_train)

"""Evaluating the trained model"""

# preduction on training data
# we are giving x_train_features to our model and it is going to predict prediction_on_training_data

prediction_on_training_data = model.predict(x_train_features)

accuracy_on_training_data = accuracy_score(y_train, prediction_on_training_data)

print('accuracy on training data: ',accuracy_on_training_data)

# preduction on test data
# we are giving x_test_features to our model and it is going to predict prediction_on_test_data

prediction_on_test_data = model.predict(x_test_features)

accuracy_on_test_data = accuracy_score(y_test, prediction_on_test_data)

print('accuracy on training data: ',accuracy_on_test_data)

"""Building A Predictive System"""

input_mail = ["""Dear, Rs.1500 Welcome Bonus credited to My11circle account. IND vs PAK T20 Match. Prize Pool - Rs.2,51,00,000 (2.51CR) & Thar Click - http://1kx.in/Vioh0I """]

# convert text to feature Vector

input_data_features = feature_extraction.transform(input_mail)

# making prediction

prediction = model.predict(input_data_features)

if prediction[0] == 0:
  print("It is spam mail")
elif prediction[0] == 1:
  print("It is ham mail")
print(prediction)