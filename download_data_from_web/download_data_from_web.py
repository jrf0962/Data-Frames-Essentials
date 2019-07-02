# Download data from the url
response = rq.get(url)
# Save downloaded content into a file
with open(os.path.join('file.csv.bz2'), mode = 'wb') as file:
     file.write(response.content)
    
# Read data into a data farme
df = pd.read_csv('file.csv.bz2')
