from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import  ImageContent, Article
from .api_image import searchImage
from .scraping_blog import run
import json

json_root = '.\data.json'
def json_(root):
    if root:
        with open(root, "r", encoding='utf-8') as f:
            json_f = json.load(f)
      
        
        return json_f
    return None

def index(request):
    image_all = ImageContent.objects.filter(image_id__icontains="")
    all_article = Article.objects.all()
    try:
        article_content = json_(json_root)
        date = article_content[0]['date_pusblishe']
        title = article_content[0]['title']
        article_shapo = article_content[0]['article_shapo']
        content = article_content[0]['article_content']
        
        if request.method == 'POST':
            if image_all.exists():
                image_all.delete()

            try:

                search_img = "Dieu"
                image = searchImage(search_img)
                title = search_img
               
                


            except:
                
                messages.info(request, "Erreure verifier votre connextion")
            new_image = ImageContent.objects.create(title=title, url_image=image)
            new_image.save()
            new_article = Article.objects.create(image=image, title=title, article_shapo=article_shapo, content=content, data_plush=date)
            new_article.save()

        context = {
                    "new_articles": all_article}       
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')

