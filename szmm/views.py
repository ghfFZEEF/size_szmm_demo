from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from szmm.models import GoodsTypes


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | list] = {
        "page_title": "Главная страница",
        "data": GoodsTypes.objects.all(),
    }

    return render(request, "szmm/index.html", context)
