import pandas as pd
import requests

# Read excel file
excelFileName = 'C:/Users/Naomi Ezaki/Documents/Data/2017.xlsx'
excelSheetName = 'Copy of 2017'
savePath = 'C:/Users/Naomi Ezaki/Documents/Data/marine_animals_data_cropped/test_images/'
xl = pd.ExcelFile(excelFileName) #excel file name
df = xl.parse(excelSheetName) #excel sheet name

# Loop through columns and download pictures
excelImageCellHeader = 'Original_Link' #Image cell header
for pic in df[excelImageCellHeader].head(): #to download all images. use .head() to download only 5 images
    url = pic
    r = requests.get(url, allow_redirects=True)
    if url.find('/'):
        filename = url.rsplit('/', 1)[1]
        # print(filename)
    if filename.find('?'):
        filename = filename.rsplit('?',1)[0]
        print(filename)
    open(savePath+filename, 'wb').write(r.content)