from django.contrib import admin
from .models import Maqola,Mahsulot

# Register your models here.
@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ['nom','muallifi','yaratilgan']
    search_fields = ['nom','muallifi','sarlavha']
    list_filter = ['holat','yaratilgan']
@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['nom','narx','yaratilgan']
    search_fields = ['nom','narx','tavsif','yaratilgan']
    list_filter = ['holat','yaratilgan']