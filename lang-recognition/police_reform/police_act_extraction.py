#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


#read in data
f = open("repubBill.txt", "r")
reptxt = ""
for x in f:
    reptxt += x


# In[8]:


reptxt


# In[9]:


g = open("demBill.txt", "r")
demtxt = ""
for x in g:
    demtxt += x


# In[10]:


demtxt


# In[11]:


#clean data (code from billsum paper)
import jsonlines
import os
import pandas as pd
import pickle
import re


# In[12]:


def replace_semicolon(text, threshold=10):
    '''
    Get rid of semicolons.
    First split text into fragments between the semicolons. If the fragment 
    is longer than the threshold, turn the semicolon into a period. O.w treat
    it as a comma.
    Returns new text
    '''
    new_text = ""
    for subset in re.split(';', text):
        subset = subset.strip() # Clear off spaces
        # Check word count
        if len(subset.split()) > threshold:
            # Turn first char into uppercase
            new_text += ". " + subset[0].upper() + subset[1:]
        else:
            # Just append with a comma 
            new_text += ", " + subset

    return new_text

USC_re = re.compile('[Uu]\.*[Ss]\.*[Cc]\.]+')
PAREN_re = re.compile('\([^(]+\ [^\(]+\)')
BAD_PUNCT_RE = re.compile(r'([%s])' % re.escape('"#%&\*\+/<=>@[\]^{|}~_'), re.UNICODE)
BULLET_RE = re.compile('\n[\ \t]*`*\([a-zA-Z0-9]*\)')
DASH_RE = re.compile('--+')
WHITESPACE_RE = re.compile('\s+')
EMPTY_SENT_RE = re.compile('[,\.]\ *[\.,]')
FIX_START_RE = re.compile('^[^A-Za-z]*')
FIX_PERIOD = re.compile('\.([A-Za-z])')
SECTION_HEADER_RE = re.compile('SECTION [0-9]{1,2}\.|\nSEC\.* [0-9]{1,2}\.|Sec\.* [0-9]{1,2}\.')

FIX_PERIOD = re.compile('\.([A-Za-z])')

SECTION_HEADER_RE = re.compile('SECTION [0-9]{1,2}\.|\nSEC\.* [0-9]{1,2}\.|Sec\.* [0-9]{1,2}\.')


# In[13]:


def clean_text(text):
    """
    Borrowed from the FNDS text processing with additional logic added in.
    Note: we do not take care of token breaking - assume SPACY's tokenizer
    will handle this for us.
    """

    # Indicate section headers, we need them for features
    text = SECTION_HEADER_RE.sub('SECTION-HEADER', text)
    # For simplicity later, remove '.' from most common acronym
    text = text.replace("U.S.", "US")
    text = text.replace('SEC.', 'Section')
    text = text.replace('Sec.', 'Section')
    text = USC_re.sub('USC', text)

    # Remove parantheticals because they are almost always references to laws 
    # We could add a special tag, but we just remove for now
    # Note we dont get rid of nested parens because that is a complex re
    #text = PAREN_re.sub('LAWREF', text)
    text = PAREN_re.sub('', text)
    

    # Get rid of enums as bullets or ` as bullets
    text = BULLET_RE.sub(' ',text)
    
    # Clean html 
    text = text.replace('&lt;all&gt;', '')

    # Remove annoying punctuation, that's not relevant
    text = BAD_PUNCT_RE.sub('', text)

    # Get rid of long sequences of dashes - these are formating
    text = DASH_RE.sub( ' ', text)

    # removing newlines, tabs, and extra spaces.
    text = WHITESPACE_RE.sub(' ', text)
    
    # If we ended up with "empty" sentences - get rid of them.
    text = EMPTY_SENT_RE.sub('.', text)
    
    # Attempt to create sentences from bullets 
    text = replace_semicolon(text)
    
    # Fix weird period issues + start of text weirdness
    #text = re.sub('\.(?=[A-Z])', '  . ', text)
    # Get rid of anything thats not a word from the start of the text
    text = FIX_START_RE.sub( '', text)
    # Sometimes periods get formatted weird, make sure there is a space between periods and start of sent   
    text = FIX_PERIOD.sub(". \g<1>", text)

    # Fix quotes
    text = text.replace('``', '"')
    text = text.replace('\'\'', '"')

    # Add special punct back in
    text = text.replace('SECTION-HEADER', '<SECTION-HEADER>')

    return text


# In[14]:


clean_reptxt = clean_text(reptxt)



# In[16]:


clean_demtxt = clean_text(demtxt)




# ## Extract Values of Attributes

# In[18]:


with open('cleanrepub.txt') as f:
    text = f.read()

sentencesRepub = re.split(r' *[\.\?!][\'"\)\]]* *', text)


# In[19]:


with open('cleandem.txt') as f:
    text = f.read()

sentencesDem = re.split(r' *[\.\?!][\'"\)\]]* *', text)


# #### generalized function

# In[66]:


#2 terms list, ranked
def generalBinaryAttribute4(sentences, topic, terms1, terms2):
    i = 0
    relevantIndexes = []
    relevantSents = []
    while i < len(sentences) - 10:
        if topic in sentences[i]:
            relevantIndexes.append(i)
            relevantSents.append(sentences[i].lower())
        i += 1
        
    
    
    #assess relevant sentences
    termCount = {}
    score = 0
    for t in terms1:
        termCount[t] = 0
    for t2 in terms2:
        termCount[t2] = 0
    g = 0
    for sent in relevantSents:
        #print(sent)
        #print('\n')
        
        #TERMS 1 SCORE INCREASE
        for t in terms1:
            if t in sent:
                termCount[t] += 1
                score += 0.5
            #make sure not at beginning/end of relevent sentences so can check adjacent sentences
            #and check the sentence before/after isn't already in relevant sentences 
            if g != 0 and relevantIndexes[g-1] != relevantIndexes[g] - 1:
                    #print(sentences[relevantIndexes[g]-1])
                    if t in sentences[relevantIndexes[g]-1].lower():
                        termCount[t] += 1
                        score += 0.5
            if g != len(relevantIndexes) - 1 and relevantIndexes[g+1] != relevantIndexes[g] + 1: 
                #print(sentences[relevantIndexes[g]+1])
                if t in sentences[relevantIndexes[g]+1].lower():
                    termCount[t] += 1
                    score += 0.5
            
        #TERMS 2 SCORE INCREASE (less than terms in term 1)
        for t2 in terms2:
            if t2 in sent:
                termCount[t2] += 1
                score += 0.05
            #make sure not at beginning/end of relevent sentences so can check adjacent sentences
            #and check the sentence before/after isn't already in relevant sentences 
            if g != 0 and relevantIndexes[g-1] != relevantIndexes[g] - 1:
                    #print(sentences[relevantIndexes[g]-1])
                    if t2 in sentences[relevantIndexes[g]-1].lower():
                        termCount[t2] += 1
                        score += 0.05
            if g != len(relevantIndexes) - 1 and relevantIndexes[g+1] != relevantIndexes[g] + 1: 
                #print(sentences[relevantIndexes[g]+1])
                if t2 in sentences[relevantIndexes[g]+1].lower():
                    termCount[t2] += 1
                    score += 0.05
            
        reductions = ['except','sensitive','unless','limit']
        for r in reductions:
            if r in sent:
                score -= 0.05
            
        g += 1
    print(termCount)
    
    if score <= 0:
        return 0
    elif score >= 1:
        return 1
    
    return score



