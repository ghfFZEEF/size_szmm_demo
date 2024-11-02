from django.contrib import admin
from .models import GoodsType, Pulsator, GrainCrushers, GrassChoppers, QrCode

admin.site.register(GoodsType)
admin.site.register(Pulsator)
admin.site.register(GrainCrushers)
admin.site.register(GrassChoppers)
admin.site.register(QrCode)
