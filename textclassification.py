# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:10:26 2019

@author: Apurva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('reviews2.csv')

#category column
y=df['Category']

#preprocessing reviews
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 490):
    review = re.sub('[^a-zA-Z]', ' ', df['comment'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
#Transforming into vectors   
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(corpus)
X_train_counts.shape

#Transforming into Tfidf values
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts).toarray()
X_train_tfidf.shape

#Splitting into values
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, y, test_size = 0.20, random_state = 0)

#Fitting Naive Bayesian algorithm
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train, y_train)

#Checking the accuracy
from sklearn.metrics import roc_curve, roc_auc_score, auc
predictions = model.predict(vect.transform(X_test))
print('AUC: ', roc_auc_score(y_test, predictions))
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)



