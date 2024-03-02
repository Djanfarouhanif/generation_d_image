from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import  ImageContent, Article
from .api_image import searchImage
from .scraping_blog import run
import json


json_root = './data.json'

#Fonction pour lire le fichier json
def json_(root):
    if root:
        with open(root, "r", encoding='utf-8') as f:
            json_f = json.load(f)
        return json_f
    return None

#Fonction de creation de l'Article
def Create_article(image):
    if json_(json_root):
        article_content = json_(json_root)
        #date = article_content[0]['date_pusblishe']
        title = article_content[0]['title']
        article_shapo = article_content[0]['article_shapo']
        content = article_content[0]['article_content']

        new_article = Article.objects.create(image=image, title=title, article_shapo=article_shapo,content=content)
        new_article.save()
    else:
        return None


def index(request):
    article = Article.objects.all()
    if request.method == "POST":
       search_img = "Le village olympique des JO de Paris 2024 inauguré par Emmanuel Macron a un futur tout tracé"
       image = searchImage(search_img)
       title = search_img
       new_image = ImageContent.objects.create(image_id=1, title=title, url_image=image)
       new_image.save()
       image_object = ImageContent.objects.get(image_id=new_image.image_id)

       Create_article(image_object)
    context = {
        "new_articles" :article
    }
    return render(request, 'index.html', context)

   
       



