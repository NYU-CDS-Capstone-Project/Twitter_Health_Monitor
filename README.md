#  TwitterHealth Monitor
This is the capstone project repository instructed by NYU Langone. In this project, our main goal is to 
Use NLP approaches to extract features relating to DIET and PHYSICAL ACTIVITY from real-time Twitter stream, and understand their temporal and spatial variation in the US.

## Repo Description
/notebooks/ : the directory for code demo
1. Raw_Data_Process.ipynb: shows how the data is processed from json fomrat to csv format
2. statics_analysis.ipynb: shows the statistic analysis in terms of the number and length of tweet, language, emojis, hashtags for different states.
3. Food_Nutrient_Report.ipynb: includes how to use USDA API to access food nutrient database and define food health scale indicator
4. USDA_foodlist_Basic.ipynb: some data visualization on food nutrient by different category level
5. tokenization + LDA.ipynb: tokenizes the text tata and runs LDA model at different scenario
6. NMF_Model_2015Data.ipynb: runs NMF model with 5 million __tokenized tweets__ from 2015 to see its performance
7. key_word_match.ipynb: a demo for key word serach(Aho–Corasick algorithm) and some analysis for the result


/pyhton script/: the code run on HPC
1. process_raw_data.py: the code used to convert original twitter data in json format to csv format for future analysis
2. filter_en_text.py: the code used to remove all the tweets that are not in english
3. token_by_spark.py: using spark to do tokenization, stemming, and lemmatization
4. token_by_whole_file.py: read entire csv file (require a lot of memeory) and then do tokenization, stemming, and lemmatization
5. token_row_by_row.py: read a csv file row by row, for each row do tokenization, stemming, and lemmatization (require less memeory)
6.key_word_process.py: read a csv file containing tweets and find whether the tweet mentions food or activity key words


/figures/: some visulization results related to the progress.

## Project Status
:white_check_mark: Completed
- Data Preprocessing: 
  - convert the raw tweets data from json to csv and extract important features including the length of tweet, emojis, hashtags etc.
  - Generating the __food list__ from [USDA](https://ndb.nal.usda.gov/ndb/doc/index) and __physical activity list__
  - Label tweets with topics by key-word search
- Baseline Modeling:
  - Topic modeling 
  - Random Forest
  
  
:white_large_square: In Progress
- Model Hyper-parameter Tuning




## Memo
