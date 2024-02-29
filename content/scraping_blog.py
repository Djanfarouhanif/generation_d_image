import requests
import json
from bs4 import BeautifulSoup
url = 'https://www.huffingtonpost.fr/jo-paris-2024/article/le-village-olympique-des-jo-de-paris-2024-inaugure-par-emmanuel-macron-ce-29-fevrier-a-un-futur-tout-trace_230481.html'

response = requests.get(url)
response.encoding = response.apparent_encoding
def scraping_content(response):
    
    
    if response.status_code == 200:
        html = response.text
        infos = {}
        soup = BeautifulSoup(html, 'html5lib')
        #Time publish
        time  = soup.find('time', class_='article-metas')
        date = time.find('span', class_='article-metas__date--update')
        infos["date_pusblishe"] = date

        #Titre de l'article
        header = soup.find('header', class_ = "article-header")
        title = header.find('h1', class_ = "article-title").text.strip()
        article_shapo = header.find('p', class_='article-shapo').text.strip()
        infos['title'] = title
        infos['article_shapo'] = article_shapo

        #Contenu de l'article

        article_conent = soup.find("div", class_= "article-content")

        all_paragraphe = []
        paragraphe = article_conent.find_all("p", class_= 'asset-text')
        for p in paragraphe:
            all_paragraphe.append(p.text.strip())

        text_paragraphe = ' '.join(all_paragraphe)

        infos['article_content'] = text_paragraphe

        data.append(infos)

        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(date,f, ensure_ascii=False, indent=4)


def load_data(infos):
    data = []

    data.append(infos)

    with open("data.json", 'w', encoding='utf-8') as f:
        json.dump(date,f, ensure_ascii=False, indent=4)



