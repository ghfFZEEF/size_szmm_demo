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
        "pulsators": {"page_title": "Доильные аппараты", "data": models.Pulsator.objects.all()},
        "grain_crushers": {"page_title": "Зернодробилки", "data": models.GrainCrushers.objects.all()},
        "grass_choppers": {"page_title": "Измельчители травы", "data": models.GrassChoppers.objects.all()},
        "pulsators_accessories": {"page_title": "Комплектующие для доильных аппаратов"},
        "grain_crushers_accessories": {"page_title": "Комплектующие/запчасти для зернодробилок"},
        "grass_choppers_accessories": {"page_title": "Запчасти для измельчителей травы"},
        "cultivators_accessories": {"page_title": "Комплектующие для мотоблоков и культиваторов"},
        "Tooth_harrow_couplings": {"page_title": "Сцепки зубовых борон"}
    }

    context: dict[str, str | list | models.QrCode | bool] = context[goods_link]
    context["qr_code"] = models.QrCode.objects.first()
    context["index"] = False
    
    return render(request, "szmm/goods.html", context)
