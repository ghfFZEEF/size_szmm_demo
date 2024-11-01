from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Model

from szmm import models


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | list | models.QrCode | bool] = {
        "page_title": "Главная страница",
        "data": models.GoodsType.objects.all(),
        "qr_code": models.QrCode.objects.first(),
        "index": True
    }

    return render(request, "szmm/index.html", context)


def goods(request: HttpRequest, goods_link: str) -> HttpResponse:
    context: dict[str, dict] = {
        "pulsators": {"page_title": "Доилки", "data": models.Pulsator.objects.all(), }
    }

    context: dict[str, str | list | models.QrCode | bool] = context[goods_link]
    context["qr_code"] = models.QrCode.objects.first()
    context["index"] = False
    
    return render(request, "szmm/goods.html", context)
