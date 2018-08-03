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

page_access_token = "EAAEJGaqiDuYBAKY9D6ZBr23G9N07yLZBOvZBGdpZCBvVmhZACkoZAKerGYOgMbRTKZBwyjezc3ei4kXE8I9XIZB6Ydh2wZAFIRg3gv5b55WUlz7WnoDKugl0hAFiRszFZAzZCd14ZArZAF3wXdcY4LZBujDrej2cZAiWjDR6TaL5LZC9VXNxErgeMbFRZBH33JZAbDihOyZAZCUR3poFAvTATAZDZD"
api_url = 'https://graph.facebook.com/v3.1'+path+'?access_token='+page_access_token+'&fields=created_time,place,full_picture,message'
page_posts = requests.get(api_url).json()


# graph=facebook.GraphAPI(page_access_token)
# page_posts = graph.get_connections("nightowl.hackerspace","posts", fields='object_id,created_time,description,message,full_picture,place')


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
