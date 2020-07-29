### Language Recognition

The third approach to obtain a descriptive summary of a bill with a variable invovles language recognition. 

The approach involves manually identifying the key issues within a topic and the key words to identify support with those issues, as well as key words to identify less support with those issues. 

#### For example

We first looked at two police reform bills, one drafted by the Republicans in the Senate found here: https://www.scott.senate.gov/imo/media/doc/JUSTICEActText.pdf and one drafted by the Democrats in the House fo Representatives found here : https://judiciary.house.gov/uploadedfiles/justice_in_policing_act_of_2020.pdf?utm_campaign=2927-519

We then manually crafted a list of the topics involved in police reform, and added binary attributes to those topics. For example, with the topic of transparency, there is a binary attribute for collection of use of force data. This means that the bill could have a 0, meaning there is no mention of collection of use of force data, or a 1, meaning there is full support and mention of collection of use of force data. The bill could also have a score anywhere between 0 and 1, since many of these issues can be complicated and do not result in clear binary results. 

The list of topics for each police reform bill, as well as the unifying topic list, is under police_reform_bill_list.txt.

We also applied this approach to gun violence bills. The Democratic bill can be found here: https://www.congress.gov/bill/116th-congress/house-bill/5717/text?format=txt and the Repbulican bill can be found here: https://www.congress.gov/bill/116th-congress/senate-bill/1519/text?q=%7B%22search%22%3A%5B%22protecting+communities%22%5D%7D&r=7&s=1. The list of topics for those bills is under gun_violence_bill_list.txt.

### Extraction Method

The extraction method created is under extractionMethod.py. 

#### Getting Started

The code for police reform bill extraction is under police_act_extraction.py. Before running that code, the bill text needs to be downlaoded. You can download the original bill texts, dempolbill.txt and repubpolbill.txt, and apply the clean_text.py code in the python file incorporated from the BillSum github, sourced here https://github.com/FiscalNote/BillSum. Or, you can download the clean bill texts, cleanpoldem.txt and cleanpolrepub.txt. 

The same applies for the gun violence data. The code for gun violence bill extraction is under gun_violence_extraction.py.  

#### Method Explanation 
 
The method has four parameters: sentences, topic, terms1, and terms2. 'sentences' is a list of sentences that makes up the bill text after cleaning. 'topic' is the overall topic to parse for, such as 'de-escalation' for the issue of de-escalation training. 'terms1' is a list of terms that carry more weight when present, and 'terms2' is a list of terms that carry less weight than terms1 but still contribute to the score. 

First, the sentences list is parsed to find all "relevant sentences,"  or any sentence with the 'topic' present. Then, the revelant sentences are parsed to search for the presence of a word from terms1 or terms2 and the score increases by 0.5 and 0.05 respectively. To increase accuracy, the method also parses the sentences preceeding and succeeding a relevant sentence, as long as it is not already listed in the relevant sentences. Finally, a score can be reduced if on of the following words are present in the relevant sentences: ['except','sensitive','unless','limit']. These words result in a reduction because of their tendency to coincide with a lack of support for an issue. 

It is worth noting that the terms1 list has a significantly large weight of 0.5 in comparison to 0.05. This is because there are often instances where there is not enough text on an issue to indicate full support, yet the writing of the bill succinctly established full support. An example is a 'banning'. Many bills include a ban of some sort, which does not always require an extensive description. The ban is estbalished and not written about again. Therefore, a word such as 'ban' may belong in terms1, and any issue lacking extensive textual evidence may require more words entered into the terms1 list. 


### Findings 

An example query and result:

``
#Use of Force Data Collection
forceTerms = ['collect','data','report','description']
RforceResult = generalBinaryAttribute4(sentencesRepub, 'use of force', [], forceTerms)
print('Repub Use of Force Collection: ', RforceResult)
DforceResult = generalBinaryAttribute4(sentencesDem, 'use of force', [],forceTerms)
print('Dem Use of Force Collection: ', DforceResult)
``

``
{'collect': 2, 'data': 2, 'report': 5, 'description': 0}
Repub Use of Force Collection:  0.44999999999999996
{'collect': 8, 'data': 8, 'report': 11, 'description': 2}
Dem Use of Force Collection:  1
``

The result indicates that, on a scale of 0 to 1, the Republican Police Reform bill supports use of force data collection at 0.45 while the Democratic Police Reform Bill supports use of force data collection fully at 1. 

Based on reading each of the bills thoroughly, this result is accurate, along with most of the restuls for both issues. 


### Future Work

The next step is to incorporate this method and code into an accessible platform, such as a website with visualizations. The goal of this project is to protect social choice mechanisms, so the public needs to have easy access to these findings. 

Another avenue is to make the terms lists and topics automatically encoded instead of manually determining the best words to search for. This may be accomplished through parsing bulk data of bills and creating topic lists and key words. 
