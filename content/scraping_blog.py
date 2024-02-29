import requests
import json
from bs4 import BeautifulSoup
url = 'https://www.huffingtonpost.fr/jo-paris-2024/article/le-village-olympique-des-jo-de-paris-2024-inaugure-par-emmanuel-macron-ce-29-fevrier-a-un-futur-tout-trace_230481.html'

response = requests.get(url)


#------------------Recuille des donnée-------------------------
def scraping_content(response):
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        html = response.text
        infos = {}
        soup = BeautifulSoup(html, 'html5lib')
        #Time publish
        time  = soup.find('time', class_='article-metas')
        date = time.find('span', class_='article-metas__date--update')
        infos["date_pusblishe"] = date.text

        # #Titre de l'article
        header = soup.find('header', class_ = "article-header")
        title = header.find('h1', class_ = "article-title").text.strip()
        article_shapo = header.find('p').text.strip()
        infos['title'] = title
        infos['article_shapo'] = article_shapo

        #Contenu de l'article

        article_conent = soup.find("div", class_= "article-content")

        all_paragraphe = []
        paragraphe = article_conent.find_all("p", class_= 'asset-text')
        for p in paragraphe:
            all_paragraphe.append(p.text.strip()+"\n")

        text_paragraphe = ' '.join(all_paragraphe)

        infos['article_content'] = text_paragraphe

        

        return infos
    return None


#--------------Ajouter ces donnée dans un fichier json-----------------
def load_data(infos_content):
    data = []
    print("''''''''''''''''''''''''")
    data.append(infos_content)
    print(data, "---------dddddddddddddddd--------")
    l = [{"hainf": "hain"}]
    with open("data.json", 'w',encoding="utf-8") as f:
        
        json.dump(data,f, ensure_ascii=False,indent=4)

    return data

def run():
    #------------Creation d'un niveau object------------
    infos = scraping_content(response)

    data = load_data(infos)
