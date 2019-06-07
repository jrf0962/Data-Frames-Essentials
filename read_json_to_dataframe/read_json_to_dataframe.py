## Import neccessary python packages (API)
import json # import json API
import pandas as pd # import pandas API as pd

## Read the json file and extract the data needed
df_list = [] # create an empty python list
## This is list is used to store neccessary data as a list of dictionaries.
## One dictionary unit equals to one observation unit in the data frame.
## Dictionary keys will be the column names and values will be values for a particular row.

with open('tweet_json.txt', 'r') as json_file:
    for line in json_file:
        data = json.loads(line)
        tweet_id = data['id']
        retweet_count = data['retweet_count']
        favorite_count = data['favorite_count']
        
        df_list.append({'tweet_id': tweet_id,
                        'retweet_count': retweet_count,
                        'favorite_count': favorite_count})

df_retweet = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count', 'favorite_count'])
