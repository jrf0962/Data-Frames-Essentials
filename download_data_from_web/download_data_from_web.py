## Import neccessary python packages (API)
import requests as rq
import os
import pandas as pd

# Download data from the url
response = rq.get(url)
# Save downloaded content into a file
with open(os.path.join('filename.ext'), mode = 'wb') as file:
     file.write(response.content)
    
# Read data into a data frame
df = pd.read_csv('filename.ext')
