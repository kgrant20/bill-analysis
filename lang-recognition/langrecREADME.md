### Language Recognition

The third approach to obtain a descriptive summary of a bill with a variable invovles language recognition. 

The approach involves manually identifying the key issues within a topic and the key words to identify support with those issues, as well as key words to identify less support with those issues. 

## For example

We first looked at two police reform bills, one drafted by the Republicans in the Senate found here: https://www.scott.senate.gov/imo/media/doc/JUSTICEActText.pdf and one drafted by the Democrats in the House fo Representatives found here : https://judiciary.house.gov/uploadedfiles/justice_in_policing_act_of_2020.pdf?utm_campaign=2927-519

We then manually crafted a list of the topics involved in police reform, and added binary attributes to those topics. For example, with the topic of transparency, there is a binary attribute for collection of use of force data. This means that the bill could have a 0, meaning there is no mention of collection of use of force data, or a 1, meaning there is full support and mention of collection of use of force data. The bill could also have a score anywhere between 0 and 1, since many of these issues can be complicated and do not result in clear binary results. 

The list of topics for each police reform bill, as well as the unifying topic list, is under police_reform_bill_list.txt.

We also applied this approach to gun violence bills. The list of topics for those bills is under gun_violence_bill_list.txt.

### Extraction Method

The extraction method created is under extractionMethod.py. 

The code for police reform bill extraction is under police_act_extraction.py. Before running that code, the bill text needs to be downlaoded. You can download the original bill texts, dempolbill.txt and repubpolbill.txt, and apply the clean_text.py code in the python file incorporated from the BillSum github, sourced here https://github.com/FiscalNote/BillSum. Or, you can download the clean bill texts, cleanpoldem.txt and cleanpolrepub.txt. 

The same applies for the gun violence data. The code for gun violence bill extraction is under gun_violence_extraction.py.  


### Method Explanation 



### Findings and Future Work 
