import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[2015, 'Jurasic World', 'Action|Adventure|Science Fiction|Thriller'],
                           [2015, 'Insurgent', 'Adventure|Science Fiction|Thriller'],
                           [1966, 'The Sand Pebbles', 'Action|Adventure|Drama|War|Romance']]),
                  columns = ['year', 'title', 'genres'])
df

# This function takes a pandas Series or a Dataframe column as an argument
# Separate strings between '|' 
# Return a stacked series

def separate(data):
    return data.str[0:].str.split('|', expand = True).stack()

# Separate genres column and join it to the dataframe.
# Use separate function above to split the string.
df = df.join(separate(df.genres).reset_index(level=1,drop=True).rename('genre')).reset_index(drop=True)
