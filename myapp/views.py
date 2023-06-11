from django.shortcuts import render
from .helpers import ImagekitClient
from .models import MediaFile


def appView(request):
    if request.method == "POST":
        title = request.POST.get("title")
        file = request.FILES.get("file")
        imgkit = ImagekitClient(file)
        response =  imgkit.upload_media_file()
        MediaFile.objects.create(
            title=title,
            url=response["url"]
        )
    media_files = MediaFile.objects.all()
    return render(request, "app.html", context={"media":media_files})
