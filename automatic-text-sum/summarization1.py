#!/usr/bin/env python
# coding: utf-8

# # ARTICLE 2

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[47]:


#read in data file and display 
f = open("article2.txt", "r")
a1 = ""
for x in f:
    a1 += x


# In[48]:


a1


# In[49]:


article_text1 = re.sub(r'\[[0-9]*\]', ' ', a1)
article_text1 = re.sub(r'\s+', ' ', a1)


# In[50]:


# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text1 )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)


# In[51]:


formatted_article_text


# In[52]:


sentence_list = nltk.sent_tokenize(article_text1)


# In[53]:


sentence_list


# In[54]:


stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


# In[55]:


word_frequencies


# In[56]:


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


# In[66]:


sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


# In[67]:


import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)


# In[77]:


word_frequencies


# In[ ]:




