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
