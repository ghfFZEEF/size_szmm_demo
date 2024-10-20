from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str] = {
        'page_title': 'Главная страница'
    }
    return render(request, 'szmm/index.html', context)
