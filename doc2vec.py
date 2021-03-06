# -*- coding: utf-8 -*-
"""Doc2Vec

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YTVb_H-pSqRHqdPk4uBFAhFSJVvRtMd5
"""

import os
if not os.path.exists("glove.6B.zip"):
  !wget http://nlp.stanford.edu/data/wordvecs/glove.6B.zip
  get_ipython().system_raw("unzip glove.6B.zip")

glove={}

file = open("glove.6B.50d.txt","r")
for i in file:
  v = i.split(" ")
  temp=[]
  for j in v[1:]:
    temp.append(float(j))
  glove[v[0]] = temp

glove['me']

import nltk
nltk.download("punkt")
nltk.download("stopwords")
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import stopwords
stopwords = stopwords.words("english")

import numpy as np
def document_vec(text):
  doc_vec = np.zeros(50,dtype=float)
  count=0
  sentences = sent_tokenize(text)
  for i in sentences:
    
    count+=1
    words = word_tokenize(i)
    sent_vec = np.zeros(50)
    word_l=0
    for word in words:
      if word not in stopwords:
        if word in glove:
          word_l+=1
          sent_vec = np.add(glove[word.lower()] , sent_vec)
    sent_vec = np.divide(sent_vec,word_l)
    doc_vec = np.add(sent_vec,doc_vec)
#     print(sent_vec)
  return [np.divide(doc_vec,count)]

sim = document_vec("Deep learing is part of my family.")
sim1 = document_vec("Deep learning is part of a broader family of machine learning methods based on artificial neural networks. Learning can be supervised, semi-supervised or unsupervised.")
print(sim)
print(sim1)
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(sim1,sim)
l=[]
print(similarity)
for i in similarity:
  l.append(sum(i))
  print(l)
print("%.4f" % (sum(l)))