## Import neccessary python packages (API)
import json # import json API
import pandas as pd # import pandas API as pd

## Read the json file and extract the data needed

# create an empty python list.
df_list = []
# This is list is used to store neccessary data as a list of dictionaries.
# One dictionary unit equals to one observation unit in the data frame.
# Dictionary keys will be the column names and values will be values for a particular row.

# The json file is stored as a text file with a file name "tweet_json.txt".
# Let's open this file as "json_file".
with open('tweet_json.txt', 'r') as json_file:
    # Read line by line in this json_file using a `for` loop.
    for line in json_file:
        # Inside this loop, we read each line on the file.
        # Load that line into a variable called "data".
        # This "data" variable is actually a python dictionary.
        data = json.loads(line)
        tweet_id = data['id']
        retweet_count = data['retweet_count']
        favorite_count = data['favorite_count']
        
        df_list.append({'tweet_id': tweet_id,
                        'retweet_count': retweet_count,
                        'favorite_count': favorite_count})

## Create the Data Frame using the df_list
df_retweet = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count', 'favorite_count'])
