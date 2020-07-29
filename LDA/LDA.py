#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import os


# In[2]:


#load each HOUSE OF REP bill's text into a dataframe

#create dataframe
dfhr = pd.DataFrame(columns = ['BillText'])

#find each folder and extract the data json file
emptyCount = 0
i = 1
#7010 is the current amount of bills
while i != 7010:
    try:
        #load a json file
        directory = '/Users/Katie/Desktop/' #use your path to the congress folder here
        with open(directory + 'congress/data/116/bills/hr/hr' + str(i) + '/data.json') as f:
            data = json.load(f)
            #print(i)
            #print(data['summary']['text'])
            
        #extract bill summary text and add to dataframe
        if data['summary'] is not None:
            info = data['summary']['text']
            dfhr = dfhr.append({'BillText': info}, ignore_index=True)
        else:
            emptyCount = emptyCount + 1
        
        i = i + 1
        
    except FileNotFoundError:
        i = i + 1
        pass
        
dfhr


# In[ ]:


#load each SENATE bill's text into a dataframe

#create dataframe
dfs = pd.DataFrame(columns = ['BillText'])

#find each folder and extract the data json file
emptyCountS = 0
j = 1
#3845 is the amount of Senate bills
while j != 3845:
    try:
        #load a json file
        with open(directory + 'congress/data/116/bills/s/s' + str(j) + '/data.json') as f:
            dataS = json.load(f)
            #print(i)
            #print(data['summary']['text'])
            
        #extract bill summary text and add to dataframe
        if dataS['summary'] is not None:
            infoS = dataS['summary']['text']
            dfs = dfs.append({'BillText': infoS}, ignore_index=True)
        else:
            emptyCountS = emptyCountS + 1
        
        j = j + 1
        
    except FileNotFoundError:
        j = j + 1
        pass
        
dfs


# In[ ]:


print('Amount of House Bills: ', 7009-emptyCount)
print('Amount of Senate Bills: ', 3844-emptyCountS)


# In[ ]:


#find same bills
sameBillsHrIndex = []
sameBillsSIndex = []
for indexHR, rowHR in dfhr.iterrows():
    if len(sameBillsHrIndex) > 20:
        break
    for indexS, rowS in dfs.iterrows():
        if rowHR['BillText'] == rowS['BillText']:
            sameBillsHrIndex.append(indexHR)
            sameBillsSIndex.append(indexS)


# In[ ]:


print("The hr indexes of hr bills that word for word equal a s bill: ", sameBillsHrIndex)


# In[ ]:


print("The s indexes of s bills that word for word equal a hr bill: ", sameBillsSIndex)


# In[ ]:


dfhr['BillText'][8]


# In[ ]:


dfs['BillText'][104]


# # Data Preprocessing

# In[3]:


import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)


# In[4]:


import nltk
nltk.download('wordnet')


# In[5]:


dfhr['index'] = dfhr.index
documents = dfhr
documents[:5]


# In[6]:


#Words are lemmatized — words in third person are changed to first person and verbs in past and future tenses are changed into present.
#Words are stemmed — words are reduced to their root form.
stemmer = SnowballStemmer('english')
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


# In[7]:


#Tokenization: Split the text into sentences and the sentences into words. Lowercase the words and remove punctuation.
#Words that have fewer than 3 characters are removed.
#All stopwords are removed.
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


# In[8]:


doc_sample = documents[documents['index'] == 3000].values[0][0]

print('original document: ')
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print('\n\n tokenized and lemmatized document: ')
print(preprocess(doc_sample))


# In[9]:


processed_docs = documents['BillText'].map(preprocess)


# In[10]:


processed_docs[:10]


# # Bag of Words

# In[11]:


dictionary = gensim.corpora.Dictionary(processed_docs)
count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break


# In[12]:


dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)


# In[13]:


bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
bow_corpus[3000]


# In[14]:


bow_doc_4310 = bow_corpus[4310]
for i in range(len(bow_doc_4310)):
    print("Word {} (\"{}\") appears {} time.".format(bow_doc_4310[i][0], 
                                               dictionary[bow_doc_4310[i][0]], 
bow_doc_4310[i][1]))


# # TF-IDF

# In[15]:


from gensim import corpora, models
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]
from pprint import pprint
for doc in corpus_tfidf:
    pprint(doc)
    break
id2word = corpora.Dictionary(processed_docs)


# # Running LDA 

# In[18]:


from gensim.models.wrappers import LdaMallet
from gensim.models.coherencemodel import CoherenceModel
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        mallet_path = r'/Users/Katie/Desktop/mallet-2.0.8/bin/mallet' 
        model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=bow_corpus, num_topics=num_topics, id2word=id2word)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
        print('|')

    return model_list, coherence_values


# In[19]:


# Can take a long time to run.
model_list, coherence_values = compute_coherence_values(dictionary=id2word, corpus=bow_corpus, texts=processed_docs, start=2, limit=200, step=6)


# In[20]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# Show graph
limit=200; start=2; step=6;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()

# Print the coherence scores
for m, cv in zip(x, coherence_values):
    print("Num Topics =", m, " has Coherence Value of", round(cv, 4))
    
# Select the model and print the topics
optimal_model = model_list[3]
model_topics = optimal_model.show_topics(formatted=False)
pprint(optimal_model.print_topics(num_words=10))


# In[21]:


lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=152, id2word=dictionary, passes=2, workers=2, alpha = 0.1,eta = 0.01,random_state=123)


# In[22]:


for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))


# # Classification of the Topics
# ## Performance Evaluation

# In[26]:


processed_docs[0]


# In[28]:


for index, score in sorted(lda_model[bow_corpus[2]], key=lambda tup: -1*tup[1]):
    print("\nScore: {}\t \nTopic: {}".format(score, lda_model.print_topic(index, 10)))


# In[29]:


processed_docs[7]


# In[30]:


for index, score in sorted(lda_model[bow_corpus[7]], key=lambda tup: -1*tup[1]):
    print("\nScore: {}\t \nTopic: {}".format(score, lda_model.print_topic(index, 10)))


# In[31]:


for index, score in sorted(lda_model[bow_corpus[1]], key=lambda tup: -1*tup[1]):
    print("\nScore: {}\t \nTopic: {}".format(score, lda_model.print_topic(index, 10)))
