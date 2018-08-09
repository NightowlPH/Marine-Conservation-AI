# -*- coding: utf-8 -*-

# Install Facebook SDK: 
# pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

#Getting access_token from pages
# graph.facebook.com/v3.1/me/accounts?access_token='your_access_token"
# copy access_token of page

import facebook
import requests
import pandas as pd
import requests
from urllib.parse import urlparse


page_url = 'https://www.facebook.com/nightowl.hackerspace/posts'
path=urlparse(page_url).path

page_access_token = "EAAEJGaqiDuYBALIKiX2ZCzciZBMr3jZCBv3Jwf6rPLvHcZB6ndZAbk8yuLpot06uZCcZCU1a7PsZAc8tGfFGwUDtNoZB3Glle2XR8DuMIAzeEGcWBZC2mdNfdOVyNHiXM3aCxdSHsLWqc2QkhWl5Q36GhJfi7oGotgvOQ2TnClI1Mlj6uT923cszj0neZAZBZCLJuLhi5HFnv5U0OXAZDZD"
api_url = 'https://graph.facebook.com/v3.1'+path+'?access_token='+page_access_token+'&fields=created_time,place,full_picture,message'
page_posts = requests.get(api_url).json()


all_post_data = []

i=0
while True:
    try:
        for p in page_posts['data']:
            all_post_data.append(p)
        page_posts = requests.get(page_posts['paging']['next']).json()
        print(i)
        i+=1
    except:
        print('DONE')
        break

# Export as Excel
# df = pd.DataFrame.from_dict(post_data)
df = pd.DataFrame(all_post_data)
df.to_excel('demo.xlsx')
