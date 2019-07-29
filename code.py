import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)

# Load the data. Data is already given to you in variable `path` 
df = pd.read_csv(path)

# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter

print('The unique ad campaigns this data has are\n', df.xyz_campaign_id.unique())
print('Number of times each campaign ran are\n', df.xyz_campaign_id.value_counts())

# What are the age groups that were targeted through these ad campaigns?
print('Age groups targeted through these ad campaigns are\n', df.age.unique())

# What was the average, minimum and maximum amount spent on the ads?
print('The average amount spent on ads is', df.Spent.mean())
print('The minimum amount spent on ads is', df.Spent.min())
print('The maximum amount spent on ads is',df.Spent.max())

# What is the id of the ad having the maximum number of clicks ?
print('Maximum number of clicks', df['Clicks'].max())
df['Clicks'].idxmax() # 860 
print('The id of the ad having maximum number of clicks is', df['ad_id'][860]) 

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
print('Total Number of people that bought the product after seeing the ad are', df['Approved_Conversion'].max())

# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases
# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 
df['Click Through Rate'] = (df['Clicks']/df['Impressions'])*100
print(df['Click Through Rate'])

# Create a new column that represents Cost Per Mille (CPM) 
df['Cost Per Mile'] = (df['Spent']/df['Impressions'])*1000
print(df['Cost Per Mile'])

