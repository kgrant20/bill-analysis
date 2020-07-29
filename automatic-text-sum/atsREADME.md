### Automatic Text Summarization

ATS is used to shorten a passage while retaining important information. Extractive summarization involves a ranking of sentences with position and importance. 

### BillSum: A Corpus for Automatic Summarization of US Legislation

There is already a paper utilizing ATS to summarize congressional bills. The paper can be found here: https://arxiv.org/abs/1910.00523 and the code can be found here: https://github.com/FiscalNote/BillSum

I planned on implementing this code to see areas for enhancement. Unfortunately, the method to pre-train language representation of NLP tasks, also known as BERT, required more RAM than I had available at the time. Although I was unable to see the code fully work, I was able to use the code that cleans the bill texts in the next approach. 

### Small Assessments

Instead of running BillSum's entire code and using all of its data, I read in a couple of bill texts, applied automatic text summarization, and assessed how accurate it was by comparing it to human made summaries. The results were acceptable. One note is the bill language often invovles amending or repealing sections of other bills, which is something that can be automatically inserted with code. 

To run these assements, download article2.txt and article3.txt. Then run summarization1.py and summarization2.py. 
