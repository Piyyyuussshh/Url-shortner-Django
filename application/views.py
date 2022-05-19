from django.http import HttpResponse
from django.shortcuts import render
import uuid
from .models import Url
# Create your views here.


def home(req):
    return render(req, 'main.html')


def create(req):
    if req.method == "POST":
        link = req.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
