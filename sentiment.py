# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:10:26 2019

@author: Apurva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('reviews2.csv')

df.stars=df.stars.astype(float)
df.dropna(inplace=True)
df = df[df['stars']!= 3]
df['Positively_Rated'] = np.where(df['stars']>3, 1, 0)

pd.crosstab(index = df['Positively_Rated'], columns="Total count")

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 454):
    review = re.sub('[^a-zA-Z]', ' ', df['comment'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 2000)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:,2].values    

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
    
y_pred = classifier.predict(X_test)
    
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print("Acccuracy = ",(cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]))
    
    
    
    
"""  
    
df.set_index('new', inplace = True)
df.set_index(keys=k)
df['new']=k
    
from sklearn.model_selection import train_test_split
# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['Positively_Rated'], random_state=0)

from sklearn.feature_extraction.text import CountVectorizer
# Fit the CountVectorizer to the training data
vect = CountVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)

X_train_vectorized = vect.transform(X_train)
from sklearn.linear_model import LogisticRegression,SGDClassifier
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train_vectorized, y_train)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train_vectorized, y_train)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train_vectorized, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import roc_curve, roc_auc_score, auc
predictions = model.predict(vect.transform(X_test))
print('AUC: ', roc_auc_score(y_test, predictions))
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)

df1=df['stars']
l=[]

for i in df1:
    f=i[0:3]
    l.append(f)

df['stars']=l
"""



