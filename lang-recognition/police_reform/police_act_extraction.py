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


# In[15]:


clean_reptxt


# In[16]:


clean_demtxt = clean_text(demtxt)


# In[17]:


clean_demtxt


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


# In[78]:


#Use of Force Data Collection
forceTerms = ['collect','data','report','description']
RforceResult = generalBinaryAttribute4(sentencesRepub, 'use of force', [], forceTerms)
print('Repub Use of Force Collection: ', RforceResult)
DforceResult = generalBinaryAttribute4(sentencesDem, 'use of force', [],forceTerms)
print('Dem Use of Force Collection: ', DforceResult)


# In[146]:


#data avilability
availabilityTerms = ['public','review','available','access','release']
RAvailabilityResult = generalBinaryAttribute4(sentencesRepub, 'data', [], availabilityTerms)
print('Repub Data Availability: ', RAvailabilityResult)
DAvailabilityResult = generalBinaryAttribute4(sentencesDem, 'data', [], availabilityTerms)
print('Dem Data Availability: ', DAvailabilityResult)


# In[82]:


#data retention 
retentionTerms = ['require','year','data','footage','report']
RetentionResult = generalBinaryAttribute4(sentencesRepub, 'retention', [], retentionTerms)
print('Repub Data Retention: ', RetentionResult)
DretentionResult = generalBinaryAttribute4(sentencesDem, 'retention', [], retentionTerms)
print('Dem Data Retention: ', DretentionResult)


# In[83]:


#body-worn cameras required
cameraTerms = ['require','car','video','audio','activate']
RCameraResult = generalBinaryAttribute4(sentencesRepub, 'camera', [], cameraTerms)
print('Repub Camera Requirement: ', RCameraResult)
DCameraResult = generalBinaryAttribute4(sentencesDem, 'camera', [], cameraTerms)
print('Dem Camera Requirement: ', DCameraResult)


# In[90]:


#anti-fraud provisions 
fraudTerms = ['fals','intent','obstruction','conceal','cover up','offense']
RFraudResult = generalBinaryAttribute4(sentencesRepub, 'report', [], fraudTerms)
print('Repub Fraud Requirement: ', RFraudResult)
DFraudResult = generalBinaryAttribute4(sentencesDem, 'report', [], fraudTerms)
print('Dem Fraud Requirement: ', DFraudResult)


# In[39]:


#whistleblowers 
whistTerms = ['authorize','right','disclose']
RWhistResult = generalBinaryAttribute4(sentencesRepub, 'release', [],whistTerms)
print('Repub Whistleblower Protection: ', RWhistResult)
DWhistResult = generalBinaryAttribute4(sentencesDem, 'release', [],whistTerms)
print('Dem Whistleblower Protection: ', DWhistResult)


# In[95]:


#requirement to intervene 
interveneTerms1 = ['excessive']
interveneTerms = ['force','training','clear','duty','file','fulfill']
RInterveneResult = generalBinaryAttribute4(sentencesRepub, 'intervene', interveneTerms1, interveneTerms)
print('Repub Intervene Requirement: ', RInterveneResult)
DInterveneResult = generalBinaryAttribute4(sentencesDem, 'intervene', interveneTerms1, interveneTerms)
print('Dem Intervene Requirement: ', DInterveneResult)


# In[96]:


#Accountability
#Enforcement of compliance
enforcementTerms = ['grant','require','reallocat','fund','ensure','fail','reduction','suspend']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'comply', [],enforcementTerms)
print('Repub Compliance Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'comply', [],enforcementTerms)
print('Dem Compliance Enforcement: ', DEnforcementResult)


# In[97]:


#handling/investigating reports of abuse 
reportsTerms = ['retain','review','investigat','maintain','record','report','force','retention']
RreportsResult = generalBinaryAttribute4(sentencesRepub, 'incident', [],reportsTerms)
print('Repub Handling Reports: ', RreportsResult)
DreportsResult = generalBinaryAttribute4(sentencesDem, 'incident', [],reportsTerms)
print('Dem Handling Reports: ', DreportsResult)


# In[67]:


#qualified immunity restriction 
immunityTerms1 = ['reform','amend']
immunityTerms2 = ['add','not be a defense']
RimmunityResult = generalBinaryAttribute4(sentencesRepub, 'immunity', immunityTerms1,immunityTerms2)
print('Repub Qualified Immunity: ', RimmunityResult)
DimmunityResult = generalBinaryAttribute4(sentencesDem, 'immunity', immunityTerms1,immunityTerms2)
print('Dem Qualified Immunity: ', DimmunityResult)


# In[68]:


#restricting chokeholds 
chokeholdTerms1 = ['ban','prohibit']
chokeholdTerms2 = ['incentiviz','prevent','civil rights violation','danger']
RChokeholdResult = generalBinaryAttribute4(sentencesRepub, 'chokehold', chokeholdTerms1,chokeholdTerms2)
print('Repub Restricting Chokeholds: ', RChokeholdResult)
DChokeholdResult = generalBinaryAttribute4(sentencesDem, 'chokehold', chokeholdTerms1,chokeholdTerms2)
print('Dem Restricting Chokeholds: ', DChokeholdResult)


# In[102]:


#restricting use of force
lessforceTerms1 = ['avoid', 'restrict']
lessforceTerms2 = ['alternatives','dangerous','reduction','de-escalat','train']
RlessforceResult = generalBinaryAttribute4(sentencesRepub, 'use of force', lessforceTerms1, lessforceTerms2)
print('Repub Restricting Use of Force: ', RlessforceResult)
DlessforceResult = generalBinaryAttribute4(sentencesDem, 'use of force', lessforceTerms1, lessforceTerms2)
print('Dem Restricting Use of Force: ', DlessforceResult)


# In[74]:


#no-knock warrant banning 
warrantTerms1 = ['ban','prohibit']
warrantTerms2 = ['report','danger','require']
RWarrantResult = generalBinaryAttribute4(sentencesRepub, 'no-knock warrant', warrantTerms1, warrantTerms2)
print('Repub no-knock warrant restrictions: ', RWarrantResult)
DWarrantResult = generalBinaryAttribute4(sentencesDem, 'no-knock warrant', warrantTerms1, warrantTerms2)
print('Dem non-knock warrant restrictions: ', DWarrantResult)


# In[75]:


#lynching federal crime 
lynchTerms = ['federal crime','crime']
RlynchResult = generalBinaryAttribute4(sentencesRepub, 'lynching', lynchTerms,[])
print('Repub no-knock warrant restrictions: ', RlynchResult)
DlynchResult = generalBinaryAttribute4(sentencesDem, 'lynching', lynchTerms,[])
print('Dem non-knock warrant restrictions: ', DlynchResult)


# In[113]:


#hiring background requirements *dem should be higher
hireTerms1 = []
hireTerms2 = ['require','study','implement','psychological','standards','disciplinary record','grant']
RhireResult = generalBinaryAttribute4(sentencesRepub, 'hiring', hireTerms1, hireTerms2)
print('Repub Hiring Background Check: ', RhireResult)
DhireResult = generalBinaryAttribute4(sentencesDem, 'hiring', hireTerms1, hireTerms2)
print('Dem Hiring Background Check: ', DhireResult)


# In[114]:


#hiring diversity requirements
divTerms = ['diverse','diversity','communit','represent']
RdivResult = generalBinaryAttribute4(sentencesRepub, 'hiring', [], divTerms)
print('Repub Hiring Diversity Requirements: ', RdivResult)
DdivResult = generalBinaryAttribute4(sentencesDem, 'hiring', [], divTerms)
print('Dem Hiring Diversity Requirements: ', DdivResult)


# In[115]:


#TRAINING
#use of force training
forcetrainTerms = ['training','require','regulat','procedure','standards','program']
RforcetrainResult = generalBinaryAttribute4(sentencesRepub, 'use of force', [], forcetrainTerms)
print('Repub use of force training: ', RforcetrainResult)
DforcetrainResult = generalBinaryAttribute4(sentencesDem, 'use of force', [] , forcetrainTerms)
print('Dem use of force training: ', DforcetrainResult)


# In[130]:


#de-escalation training
deecsTerms1 = ['training','effort']
deescTerms = ['technique','minimize','program','avoid','develop']
RdeescResult = generalBinaryAttribute4(sentencesRepub, 'de-escalat', deecsTerms1, deescTerms)
print('Repub de-escalation training: ', RdeescResult)
DdeescResult = generalBinaryAttribute4(sentencesDem, 'de-escalat', deecsTerms1,deescTerms)
print('Dem de-escalation training: ', DdeescResult)


# In[132]:


#anti-descrimmination training 
antidescTerms1 = ['training']
antidescTerms = ['racial','awareness','program','standards']
RantidescResult = generalBinaryAttribute4(sentencesRepub, 'bias', antidescTerms1, antidescTerms)
print('Repub anti-descrimmination training: ', RantidescResult)
DantidescResult = generalBinaryAttribute4(sentencesDem, 'bias', antidescTerms1, antidescTerms)
print('Dem anti-descrimmination training: ', DantidescResult)


# In[144]:


#requirements for victim services 
victimTerms1 = ['provide']
victimTerms = ['service','counseling','protect']
RvictimResult = generalBinaryAttribute4(sentencesRepub, 'victim', victimTerms1,victimTerms)
print('Repub victim services: ', RvictimResult)
DvictimResult = generalBinaryAttribute4(sentencesDem, 'victim', victimTerms1,victimTerms)
print('Dem victim services: ', DvictimResult)

