#  TwitterHealth Monitor
This is the capstone project repository instructed by NYU Langone. In this project, our main goal is to 
Use NLP approaches to extract features relating to DIET and PHYSICAL ACTIVITY from real-time Twitter stream, and understand their temporal and spatial variation in the US. 

## Project Status Memo
:white_check_mark: Completed
- Data Preprocessing: 
  - Convert the raw tweets data from json to csv and extract important features including the length of tweet, emojis, hashtags etc.
  - Generating the __food list__ from [USDA](https://ndb.nal.usda.gov/ndb/doc/index) and __physical activity list__ from [harvard.edu](https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-of-leisure-and-routine-activities)
  - Label tweets with food/activity by key-word search
- Statistic analysis on the tweets
  - the most-used languages on Twitter inside U.S.
  - the average length of each tweet for each state
  - frequency analysis on hashtag, emoji
  - from the result of key-word search, analyze the percentage of tweet mentioning food or activity for each state.
- Baseline Modeling:
  - Topic modeling: Tried NMF and LDA model. Tuned different combination of hyperparameters of LDA.
  - Random Forest: Used LDA transformation to extract each tweet's topic probability distribution as features. Then constructed the machine learning classifiers.
- Optimization:
  - Tried different hyper-parameters for LDA to extract the higher-quality features and feed into classifiers.
  - Tuned Random Forest Hyper-parameter to have better classification to identify food tweets and activity tweets.
- Results:
  - Subsampling to generate the confidence interval of the percentage of tweet mentioning food or activity for each state.
  - Used embedding distances and false positives to evaluate models' performance
  - Generated graph to demonstrated the seasonal and state-wise difference of food/activity related tweets.
  
## Repo Description
/notebooks/ : the directory for code demo
1. Activity_Classifier_Random_Forest_newest.ipynb: uses random forest to predict whether a tweet contains activity or not
2. Activity_List_General.ipynb: uses website scrapping to obtain a list of activity
3. Activity_List_Specific.ipynb: a more specific list of activity
4. Food_Nutrient_Report.ipynb: includes how to use USDA API to access food nutrient database and define food health scale indicator
5. NMF.ipynb: nmf model based on small sample
6. NMF_Model_2015Data.ipynb: runs NMF model with 5 million __tokenized tweets__ from 2015 to see its performance
7.RF_Baseline_for_Food.ipynb: uses random forest to predict whether a tweet contains food or not
8. Raw_Data_Process_new_version.ipynb: shows how the data is processed from json fomrat to csv format
9. USDA_foodlist_Basic.ipynb: some data visualization on food nutrient by different category level
10. key_word_match.ipynb: a demo for key word serach(Aho–Corasick algorithm) and some analysis for the result
11. statics_analysis.ipynb: shows the statistic analysis in terms of the number and length of tweet, language, emojis, hashtags for different states.
12. tokenization + LDA.ipynb: tokenizes the text tata and runs LDA model at different scenario
13. Run_Statistic.ipynb: Applied the Kolmogorov-Smirnov test to each LDA model and visulization.
14. usa_heatmap.ipynb: generate usa heatmap to show the seasonal and state-wise difference.
15. day_of_week_change.ipynb: generate plots to show the day-of-week change of the percentage of tweet mentioning food/activity for each state.
16. resample_confidence_interval.ipynb: subsampling to generate teh confidence interval of the percentage of tweet mentioning food/activity for each state.
17. glove_distance_calc.ipynb: calculate word embedding distance between tweets and key-word list using Glove.
18. Random_Forest_Embedding_Distance.ipynb: evaluate rf's performance using embedding distances.
19. key_word_search vs random_forest.ipynb: compare the results of key-word search and random forest model.


/pyhton script/: the code run on HPC
1. Run_LDA.py: running and tuning LDA
2. filter_en_text.py: the code used to remove all the tweets that are not in english
3. key_word_process.py: key word search by Aho-Corasick algorithem to detect tweets contain food or activity
4. process_raw_data.py: the code used to convert original twitter data in json format to csv format for future analysis
5. token_by_spark.py: using spark to do tokenization, stemming, and lemmatization
6. token_by_whole_file.py: read entire csv file (require a lot of memeory) and then do tokenization, stemming, and lemmatization
7. token_row_by_row.py: read a csv file row by row, for each row do tokenization, stemming, and lemmatization (require less memeory)
8.key_word_process.py: read a csv file containing tweets and find whether the tweet mentions food or activity key words
9. ks_test.py: Kolmogorov-Smirnov test and return empirical p-values for food and activity seperately for each LDA model.


/figures/: some visulization results related to the progress.

- __Team Name： Burger King__
- __Team Members: Qintai Liu, Zhiming Guo, Xiaoxue Ma, Jin Han__
