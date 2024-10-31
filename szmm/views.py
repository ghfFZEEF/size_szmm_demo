from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Model

from szmm import models


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | list] = {
        "page_title": "Главная страница",
        "data": models.GoodsType.objects.all(),
        "index": True
    }

    return render(request, "szmm/index.html", context)


def goods(request: HttpRequest, goods_link: str) -> HttpResponse:
    context: dict[str, str | list] = {
        "pulsators": {"page_title": "Доилки", "data": models.Pulsator.objects.all(), "index": False}
    }

    return render(request, "szmm/goods.html", context[goods_link])
