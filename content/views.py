from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import  ImageContent
from .api_image import searchImage
from .scraping_blog import run
import json

# json_root = './data.json'

# #Fonction pour lire le fichier json
# def json_(root):
#     if root:
#         with open(root, "r", encoding='utf-8') as f:
#             json_f = json.load(f)
#         return json_f
#     return None

#Fonction de creation de l'Article
# def Create_article(image):
#     if json_(json_root):
#         article_content = json_(json_root)
#         #date = article_content[0]['date_pusblishe']
#         title = article_content[0]['title']
#         article_shapo = article_content[0]['article_shapo']
#         content = article_content[0]['article_content']

#         new_article = Article.objects.create(image=image, title=title, article_shapo=article_shapo,content=content)
#         new_article.save()
#     else:
#         return None


def index(request):
    images = ImageContent.objects.all()
    if request.method == "POST":
        search = request.POST['search']
        
        if searchImage(search):
            images = searchImage(search)
            
            for image in images:
                if ImageContent.objects.filter(url_image=image).exists():
                    return redirect('/')
                else:
                    new_images = ImageContent.objects.create(url_image=image)
                    new_images.save()
    
        
    context = {"images": images}

    return render(request, 'gallery.html', context)
    

   
       



