import requests
import json
from bs4 import BeautifulSoup
url = 'https://www.huffingtonpost.fr/jo-paris-2024/article/le-village-olympique-des-jo-de-paris-2024-inaugure-par-emmanuel-macron-ce-29-fevrier-a-un-futur-tout-trace_230481.html'

#------------------gestions des erreues------------------------
def get_text_if_note_none(e):
    if e:
        return e.text.strip()
    return None

#------------------Recuille des donnée-------------------------
def scraping_content(url):
    try: 
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            html = response.text
            infos = {}
            soup = BeautifulSoup(html, 'html5lib')
            #Time publish
            if soup:

                time  = soup.find('time', class_='article-metas')
                date = get_text_if_note_none( time.find('span', class_='article-metas__date--update'))
                if date:
                    infos["date_pusblishe"] = date

                # #Titre de l'article
                
                header = soup.find('header', class_ = "article-header")
                title = get_text_if_note_none(header.find('h1', class_ = "article-title"))
                article_shapo = get_text_if_note_none( header.find('p'))
                if title:
                    infos['title'] = title
                if article_shapo:
                    infos['article_shapo'] = article_shapo

                #Contenu de l'article

                article_conent = soup.find("div", class_= "article-content")

                all_paragraphe = []
                paragraphe = article_conent.find_all("p", class_= 'asset-text')
                for p in paragraphe:
                    if 'HuffPost' not in str(p):
                        all_paragraphe.append(p.text.strip())
                        
                text_paragraphe = ' '.join(all_paragraphe)
                if paragraphe:
                    infos['article_content'] = text_paragraphe

                return infos
            else:
                return None
    except:
        return None


#--------------Ajouter ces donnée dans un fichier json-----------------
def load_data(infos_content):
    data = []
    data.append(infos_content)
    with open("data.json", 'w',encoding="utf-8") as f:
        
        json.dump(data,f, ensure_ascii=False,indent=4)

    return data

def run():
    #------------Creation d'un niveau object------------
    infos = scraping_content(url)
    data = load_data(infos)

    return data and infos

run()