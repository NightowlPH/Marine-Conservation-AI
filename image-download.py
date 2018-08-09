import pandas as pd
import requests

# Read excel file
xl = pd.ExcelFile('demo.xlsx')
df = xl.parse("Sheet1")

# Loop through 'full_picture' column and download pictures
for pic in df['full_picture'].head(): #5 pictures...remove the .head() to download all images
    url = pic
    r = requests.get(url, allow_redirects=True)
    if url.find('/'):
        filename = url.rsplit('/', 1)[1]
        # print(filename)
    if filename.find('?'):
        filename = filename.rsplit('?',1)[0]
        print(filename)
    open('images/'+filename, 'wb').write(r.content)