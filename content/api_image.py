#Google search
import requests
import random
import os
import json

def searchImage(title):
    API_KEY = open('content/API_KEY').read()
    SEARCH_ENIGIME_ID = open('content/SEARCH_ENIGIME_ID').read()
    searchQurery = title
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': searchQurery,
        'key': API_KEY,
        'cx': SEARCH_ENIGIME_ID,
        'searchType': 'image'
    }
    allUrls = []
    try:
        response = requests.get(url, params=params)
    except:
        response = None

    if response:
        if response.status_code == 200:
            urls_response = response.json()['items']
            for index in range(len(urls_response)):
                allUrls.append(urls_response[index]['link'])
            

            return allUrls

        return None
    return None

     