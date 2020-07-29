### LDA Topic Modeling

The first part of the research project involved a Topic Modeling approach in order to extract meaning from the bill texts. 

### Data

The congressional bills from the 116th Congress used in this section can be downloaded in bulk here: https://www.propublica.org/datastore/dataset/congressional-data-bulk-legislation-bills

### Next Steps

Run the LDA.py code. Make sure to insert your path to the congress folder previously downloaded into the code. 

### Results

The highest optimal number of topics I was able to calculate was 152, with a coherence value of 0.554. An example of a topic can be seen below.

 Words: 0.075*"health" + 0.046*"medicar" + 0.035*"covid" + 0.033*"servic" + 0.031*"insur" + 0.030*"cost" + 0.027*"requir" + 0.027*"emerg" + 0.024*"share" + 0.022*"medicaid"
 
 
 However, some of the results are invalid. For example, for hr4, or bow_corpus[2], the dominant topic computed through LDA is: "Require state aircraft federal flight effect aviation january take year." Yet, there is no mention of aviation/aircraft/flight in the bill hr4, as it is titled "Voting RIghts Advancement Act of 2019" and it centers on voting practices. The second topic listed for this bill seems more accurate: "COVID election service state voter require vote individual corporation disease." However, this topic received a significantly lower coherence score than the first one (0.164 vs 0.2725). 
 
 These findings resulted in a different approach: automatic text summarization. 
