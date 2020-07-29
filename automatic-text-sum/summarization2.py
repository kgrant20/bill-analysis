#!/usr/bin/env python
# coding: utf-8

# # ARTICLE 3

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import urllib.request
import re


# In[22]:


#read in data file and display 
f = open("article3.txt", "r")
a2 = ""
for x in f:
    a2 += x


# In[24]:


a2


# In[30]:


article_text1 = re.sub(r'\[[0-9]*\]', ' ', a2)
article_text1 = re.sub(r'\s+', ' ', a2)


# In[31]:


article_text1


# In[32]:


# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text1 )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)


# In[61]:


formatted_article_text = re.sub(r'\([^)]*\)', "", article_text1 )


# In[62]:


formatted_article_text


# In[63]:


import nltk
sentence_list = nltk.sent_tokenize(article_text1)


# In[64]:


sentence_list


# In[65]:


stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


# In[66]:


word_frequencies


# In[67]:


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


# In[72]:


sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


# In[73]:


import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)


# In[ ]:




