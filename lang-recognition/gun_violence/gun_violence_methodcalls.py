#this file includes gun violence bills method calls and term lists

#data avilability
availabilityTerms = ['review','available','require','allow','access']
RAvailabilityResult = generalBinaryAttribute4(sentencesRepub, 'information', [], availabilityTerms)
print('Repub Data Availability: ', RAvailabilityResult)
DAvailabilityResult = generalBinaryAttribute4(sentencesDem, 'information', [], availabilityTerms)
print('Dem Data Availability: ', DAvailabilityResult)



#Federal/violation record Collection
forceTerms = ['submit','available','consistent','collect','report','description','submit','provide']
RforceResult = generalBinaryAttribute4(sentencesRepub, 'information', [], forceTerms)
print('Repub Federal record Collection: ', RforceResult)
DforceResult = generalBinaryAttribute4(sentencesDem, 'information', [],forceTerms)
print('Dem Federal record Collection: ', DforceResult)



#data retention 
retentionTerms = ['annual','require','year','consistent','database','maintain']
RetentionResult = generalBinaryAttribute4(sentencesRepub, 'record', [], retentionTerms)
print('Repub Data Retention: ', RetentionResult)
DretentionResult = generalBinaryAttribute4(sentencesDem, 'record', [], retentionTerms)
print('Dem Data Retention: ', DretentionResult)




#anti-fraud provisions 
fraudTerms1 = ['false','penalty']
fraudTerms = ['prohibit','lying','risk protection','denial']
RFraudResult = generalBinaryAttribute4(sentencesRepub, 'report', fraudTerms1, fraudTerms)
print('Repub Fraud Requirement: ', RFraudResult)
DFraudResult = generalBinaryAttribute4(sentencesDem, 'report', fraudTerms1, fraudTerms)
print('Dem Fraud Requirement: ', DFraudResult)




#Accountability
#increasing Federal prosecution of gun violence
enforcementTerms = ['prosecute','investigat','penalt','ban','imprisonment','fine','revoke','seizure']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'violation', [],enforcementTerms)
print('Repub Compliance Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'violation', [],enforcementTerms)
print('Dem Compliance Enforcement: ', DEnforcementResult)




#straw purchasing
enforcementTerms1 = ['prohibit','illegal']
enforcementTerms = ['unlawful','investigat','penalt','ban','offense','violat']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'straw', enforcementTerms1, enforcementTerms)
print('Repub Straw Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'Straw', enforcementTerms1, enforcementTerms)
print('Dem Straw Enforcement: ', DEnforcementResult)



#trafficking **dem uses various wording to describe
enforcementTerms1 = ['prohibit','illegal']
enforcementTerms = ['unlawful','investigat','penalt','ban','offense','violat']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'traffick', enforcementTerms1, enforcementTerms)
print('Repub Straw Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'traffick', enforcementTerms1, enforcementTerms)
print('Dem Straw Enforcement: ', DEnforcementResult)




#assault weapons ban 
enforcementTerms1 = ['ban','prohibit','illegal']
enforcementTerms = ['unlawful','investigat','penalt','restrict','offense','violat']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'assault weapon', enforcementTerms1, enforcementTerms)
print('Repub Straw Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'assault weapon', enforcementTerms1, enforcementTerms)
print('Dem Straw Enforcement: ', DEnforcementResult)




#silencer/muffler ban
enforcementTerms1 = ['prohibit','illegal','ban']
enforcementTerms = ['silencer','muffler','penalt']
REnforcementResult = generalBinaryAttribute4(sentencesRepub, 'silencer', enforcementTerms1, enforcementTerms)
print('Repub Straw Enforcement: ', REnforcementResult)
DEnforcementResult = generalBinaryAttribute4(sentencesDem, 'Silencer', enforcementTerms1, enforcementTerms)
print('Dem Straw Enforcement: ', DEnforcementResult)



#DEALER REFORM
#shop security
reportsTerms = ['safe','secure','investigat','maintain','record','report','force','licensed dealer']
RreportsResult = generalBinaryAttribute4(sentencesRepub, 'dealer', [],reportsTerms)
print('Repub Handling Reports: ', RreportsResult)
DreportsResult = generalBinaryAttribute4(sentencesDem, 'dealer', [],reportsTerms)
print('Dem Handling Reports: ', DreportsResult)




#DEALER REFORM
#employee check
reportsTerms = ['safe','secure','background check','qualified','test','report','enforce','licensed dealer']
RreportsResult = generalBinaryAttribute4(sentencesRepub, 'employ', [],reportsTerms)
print('Repub Handling Reports: ', RreportsResult)
DreportsResult = generalBinaryAttribute4(sentencesDem, 'employ', [],reportsTerms)
print('Dem Handling Reports: ', DreportsResult)



#INDUSTRY REFORM
# firearm transport / employee protection
reportsTerms = ['safe','secure','protect','qualified','test','authorize','enforce','lawful','violat']
RreportsResult = generalBinaryAttribute4(sentencesRepub, 'transport', [],reportsTerms)
print('Repub Handling Reports: ', RreportsResult)
DreportsResult = generalBinaryAttribute4(sentencesDem, 'transport', [],reportsTerms)
print('Dem Handling Reports: ', DreportsResult)



#gun violence study
lessforceTerms1 = ['study', 'research']
lessforceTerms2 = ['alternatives','intervention','reduction','program']
RlessforceResult = generalBinaryAttribute4(sentencesRepub, 'violence', lessforceTerms1, lessforceTerms2)
print('Repub Restricting Use of Force: ', RlessforceResult)
DlessforceResult = generalBinaryAttribute4(sentencesDem, 'violence', lessforceTerms1, lessforceTerms2)
print('Dem Restricting Use of Force: ', DlessforceResult)
