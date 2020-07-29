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
