from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import UrlModel

HOST = 'http://127.0.0.1:8000/sh/'


def index(request, hash):
    url = get_object_or_404(UrlModel, hash_url=hash)
    return redirect(url.origin_url)


def generate(request, origin_url):
    url = UrlModel.objects.filter(origin_url=origin_url).first()
    if not url:
        url = UrlModel.objects.create(origin_url=origin_url)
        url.save()
    return JsonResponse({"data": HOST + str(url.hash_url)})
