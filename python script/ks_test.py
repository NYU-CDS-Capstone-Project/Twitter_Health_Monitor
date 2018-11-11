#!/usr/bin/env python3
import pandas as pd
import numpy as np
import os.path
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl
from time import time
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import ParameterGrid
from random import sample
from matplotlib import pyplot as plt
from scipy import stats
import random
import warnings
warnings.filterwarnings('ignore')
def loading_lda(num_topics,max_features,max_df,min_df):
    term_freq_df_path = '/scratch/jh5695/LDA_matrix/tfVectorizer_topics={}_maxFeatures={}_maxDf={}_minDf={}.csv'.format(num_topics,max_features,max_df,min_df)
    if os.path.exists(term_freq_df_path):
        term_freq_df = pd.read_csv(term_freq_df_path)
    voc_list = list(term_freq_df.columns)
    all_idx = [i for i in range(len(voc_list))]
    food_idx = [idx for idx in range(len(voc_list)) if voc_list[idx] in food]
    activity_idx = [idx for idx in range(len(voc_list)) if voc_list[idx] in activity]
    irrelevant_idx = list(filter(lambda x: x not in food_idx + activity_idx,all_idx))
    empirical_food_ts_list = []
    empirical_activity_ts_list = []
    for i in range(num_topics):
        #print(i)
        food_ts_list = []
        food_p_list = []
        activity_ts_list = []
        activity_p_list = []
        all_prob = term_freq_df.iloc[i,:]
        food_prob = all_prob[food_idx].tolist()
        activity_prob = all_prob[activity_idx].tolist() 
        irrelevant_prob = all_prob[irrelevant_idx].tolist()
        food_ts,food_p = stats.ks_2samp(food_prob, irrelevant_prob)
        activity_ts,activity_p = stats.ks_2samp(activity_prob, irrelevant_prob)
        food_ts_list.append(food_ts)
        food_p_list.append(food_p)
        activity_ts_list.append(activity_ts)
        activity_p_list.append(activity_p)  
        count = 20000
        while count != 0:
            count -= 1
            np.random.seed(1)
            all_prob = np.random.permutation(all_prob)
            food_prob = all_prob[food_idx].tolist()
            activity_prob = all_prob[activity_idx].tolist() 
            irrelevant_prob = all_prob[irrelevant_idx].tolist()
            food_ts,food_p = stats.ks_2samp(food_prob, irrelevant_prob)
            activity_ts,activity_p = stats.ks_2samp(activity_prob, irrelevant_prob)

            food_ts_list.append(food_ts)
            food_p_list.append(food_p)
            activity_ts_list.append(activity_ts)
            activity_p_list.append(activity_p) 
        empirical_food_ts = len([i for i in food_ts_list[1:] if i > food_ts_list[0]])/20000
        empirical_activity_ts = len([i for i in activity_ts_list[1:] if i > activity_ts_list[0]])/20000
        empirical_food_ts_list.append(empirical_food_ts)
        empirical_activity_ts_list.append(empirical_activity_ts)
    return empirical_food_ts_list,empirical_activity_ts_list
if __name__ == '__main__':
    food = list(pkl.load(open("/scratch/jh5695/data/food.pickle","rb")))
    food = [i.strip() for i in food]
    activity = list(pkl.load(open("/scratch/jh5695/data/activity.pickle","rb")))
    activity = [i.strip() for i in activity]
    print(loading_lda(75,12000,0.4,1))
    print(loading_lda(75,16000,0.4,1))
    print(loading_lda(100,12000,0.5,1))
    print(loading_lda(100,16000,0.5,1))




