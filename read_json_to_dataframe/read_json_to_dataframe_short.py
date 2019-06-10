## Import neccessary python packages (API)
import json # import json API
import pandas as pd # import pandas API as pd

## Read the json file and extract the data needed
# Create an empty python list.
df_list = []
# Open the file as "json_file".
with open('tweet_json.txt', 'r') as json_file:
    # Read line by line in this json_file using a `for` loop.
    for line in json_file:
        # Load the line into a variable called "data".
        data = json.loads(line)
        # Relate each of the variables to corresponding values in "data" dictionary by assigning the dictionary key.
        tweet_id = data['id']
        retweet_count = data['retweet_count']
        favorite_count = data['favorite_count']
        # Add the three variables as a single observation unit into the list ("df_list").
        df_list.append({'tweet_id': tweet_id,
                        'retweet_count': retweet_count,
                        'favorite_count': favorite_count})

## Create the Data Frame using the df_list
# Convert the list into a data frame.
df_retweet = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count', 'favorite_count'])
