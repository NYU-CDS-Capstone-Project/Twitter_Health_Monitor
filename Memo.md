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
  
:white_large_square: In Progress
- Keep trying different hyper-parameters to extract the higher-quality features and feed into classifiers.
- Random Forest Hyper-parameter Tuning to have better classification to identify food tweets and activity tweets.
- Subsampling to generate the confidence interval of the percentage of tweet mentioning food or activity for each state.
