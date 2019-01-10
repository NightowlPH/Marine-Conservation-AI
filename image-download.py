import pandas as pd
import requests

# Read excel file
excelFileName = 'MarineAnimals_ImageURL.xlsx'
excelSheetName = '300 images'
xl = pd.ExcelFile(excelFileName) #excel file name
df = xl.parse(excelSheetName) #excel sheet name

# Loop through columns and download pictures
excelImageCellHeader = 'URL' #Image cell header
for pic in df[excelImageCellHeader].head(): #to download all images. use .head() to download only 5 images
    url = pic
    r = requests.get(url, allow_redirects=True)
    if url.find('/'):
        filename = url.rsplit('/', 1)[1]
        # print(filename)
    if filename.find('?'):
        filename = filename.rsplit('?',1)[0]
        print(filename)
    open('images/'+filename, 'wb').write(r.content)