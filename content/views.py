from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import  ImageContent
from .api_image import searchImage

ur  = searchImage('homme')
print(ur, "*******************")
def index(request):
    image_all = ImageContent.objects.all()
    if request.method == 'POST':
        if len(image_all) == 0:
            image_all.delete()

        try:

            search_img = request.POST["search"]
            image = searchImage(search_img)
            title = search_img
            new_image = ImageContent.objects.create(title=title, url_image=image)
            new_image.save()
            


        except:
            
            messages.info(request, "Erreure verifier votre connextion")
    context = {"new_image":image_all}       
    return render(request, 'index.html', context)